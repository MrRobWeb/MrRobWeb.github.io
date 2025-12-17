"""
Generate embeddings for portfolio data (projects and expertise) for RAG-based similarity search.

Uses Jina AI free embeddings API.

Prerequisites:
    pip install requests python-dotenv

Usage:
    1. Get free API key from https://jina.ai/embeddings/
    2. Create a .env file with JINA_API_KEY=your_api_key
    3. Run: python generate_embeddings.py
    4. Output: embeddings.json (used by the Digital Twin chat)

Data Sources:
    - projects.js: Project portfolio data
    - skills.js: Technical skills and tool stacks
"""

import json
import os
import re
import requests
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    print("Please install required packages: pip install requests python-dotenv")
    exit(1)

# Load environment variables from project root .env file
project_root = Path(__file__).parent.parent.parent
env_path = project_root / ".env"

if env_path.exists():
    load_dotenv(env_path)
    print(f"✓ Loaded .env from: {env_path}")
else:
    load_dotenv()
    print(f"⚠ No .env found at {env_path}, trying default locations...")

# Check for API key
api_key = os.getenv("JINA_API_KEY")

if not api_key:
    print("\n❌ Error: Jina API key not found!")
    print(f"   1. Get free API key from: https://jina.ai/embeddings/")
    print(f"   2. Add to .env file at: {env_path}")
    print("   With content: JINA_API_KEY=jina_xxxxx")
    exit(1)

# Jina API configuration
JINA_API_URL = "https://api.jina.ai/v1/embeddings"
EMBEDDING_MODEL = "jina-embeddings-v3"


def get_embedding(text: str) -> list[float]:
    """Generate embedding using Jina AI API."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": EMBEDDING_MODEL,
        "task": "retrieval.passage",
        "input": [text]
    }

    response = requests.post(JINA_API_URL, headers=headers, json=data)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        raise Exception(f"Jina API error: {response.status_code}")

    result = response.json()
    return result["data"][0]["embedding"]


def parse_js_array(js_content: str) -> list[dict]:
    """Parse a JavaScript array export into Python objects."""
    # Remove the export statement and get just the array
    array_match = re.search(r'export\s+const\s+\w+\s*=\s*(\[[\s\S]*\]);?\s*$', js_content)
    if not array_match:
        raise ValueError("Could not find exported array in JS file")

    array_str = array_match.group(1)

    # Step 1: Replace template literals with placeholder tokens
    template_literals = []
    def save_template_literal(match):
        content = match.group(1)
        idx = len(template_literals)
        template_literals.append(content)
        return f'{{{{TEMPLATE_{idx}}}}}'

    array_str = re.sub(r'`([^`]*)`', save_template_literal, array_str)

    # Step 2: Replace single-quoted strings with placeholder tokens
    single_quoted = []
    def save_single_quoted(match):
        content = match.group(1)
        idx = len(single_quoted)
        single_quoted.append(content)
        return f'{{{{SINGLE_{idx}}}}}'

    array_str = re.sub(r"'([^']*)'", save_single_quoted, array_str)

    # Step 3: Now safely add quotes around property names (only unquoted identifiers followed by :)
    array_str = re.sub(r'([{,]\s*)(\w+)(\s*:)', r'\1"\2"\3', array_str)

    # Step 4: Remove trailing commas before ] or }
    array_str = re.sub(r',(\s*[}\]])', r'\1', array_str)

    # Step 5: Restore single-quoted strings as double-quoted JSON strings
    for idx, content in enumerate(single_quoted):
        escaped = content.replace('\\', '\\\\').replace('"', '\\"')
        array_str = array_str.replace(f'{{{{SINGLE_{idx}}}}}', f'"{escaped}"')

    # Step 6: Restore template literals as double-quoted JSON strings
    for idx, content in enumerate(template_literals):
        escaped = content.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        array_str = array_str.replace(f'{{{{TEMPLATE_{idx}}}}}', f'"{escaped}"')

    try:
        return json.loads(array_str)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        print(f"Problematic content around error: {array_str[max(0, e.pos-100):e.pos+100]}")
        raise


def create_project_chunks() -> list[dict]:
    """Create text chunks from projects.js file."""
    projects_path = Path(__file__).parent / "projects.js"

    with open(projects_path, "r") as f:
        js_content = f.read()

    projects_data = parse_js_array(js_content)

    chunks = []
    for i, project in enumerate(projects_data):
        title = project.get("title", "")
        role = project.get("role", "")
        industry = project.get("industry", "")
        date = project.get("date", "")
        description = project.get("description", "")

        # Handle technologies - can be array of strings
        technologies = project.get("technologies", [])
        if isinstance(technologies, list):
            tech_str = ", ".join(technologies)
        else:
            tech_str = str(technologies)

        content = f"""{title} - {role} ({date}).
{description}
Technologies: {tech_str}.
Industry: {industry}."""

        chunks.append({
            "id": f"project-{i+1}",
            "type": "project",
            "title": title,
            "role": role,
            "industry": industry,
            "date": date,
            "content": content
        })

    print(f"  Loaded {len(chunks)} projects from projects.js")
    return chunks


def create_skills_chunks() -> list[dict]:
    """Create text chunks from skills.js file."""
    skills_path = Path(__file__).parent / "skills.js"

    with open(skills_path, "r") as f:
        js_content = f.read()

    skills_data = parse_js_array(js_content)

    chunks = []
    for i, stack in enumerate(skills_data):
        title = stack.get("title", "")
        sub_title = stack.get("subTitle", "")
        description = stack.get("description", "")
        skills = stack.get("skills", {})

        # Extract all skills from nested structure
        all_skills = []
        for category, category_data in skills.items():
            category_desc = category_data.get("description", "")
            values = category_data.get("values", [])
            skill_names = [v.get("name", "") for v in values]
            skill_levels = [(v.get("name", ""), v.get("skillValue", "0")) for v in values]

            # Group by proficiency level
            high_skills = [name for name, level in skill_levels if float(level) >= 0.8]
            medium_skills = [name for name, level in skill_levels if 0.5 <= float(level) < 0.8]

            all_skills.append({
                "category": category,
                "description": category_desc,
                "skills": skill_names,
                "high_proficiency": high_skills,
                "medium_proficiency": medium_skills
            })

        # Build content string
        skills_text = ""
        for skill_cat in all_skills:
            cat_name = skill_cat["category"].replace("programmingLanguages", "Programming Languages").replace("frameworks", "Frameworks").replace("libraries", "Libraries & Tools")
            skills_text += f"\n{cat_name}: {', '.join(skill_cat['skills'])}."
            if skill_cat["high_proficiency"]:
                skills_text += f" High proficiency: {', '.join(skill_cat['high_proficiency'])}."

        content = f"""{title} - {sub_title}
{description}
Technical Skills:{skills_text}"""

        chunks.append({
            "id": f"skills-{i+1}",
            "type": "skills",
            "title": title,
            "subTitle": sub_title,
            "content": content
        })

    print(f"  Loaded {len(chunks)} skill stacks from skills.js")
    return chunks


def create_expertise_chunks() -> list[dict]:
    """Create text chunks from expertise.js file."""
    expertise_path = Path(__file__).parent / "expertise.js"

    with open(expertise_path, "r") as f:
        js_content = f.read()

    expertise_data = parse_js_array(js_content)

    chunks = []
    for i, area in enumerate(expertise_data):
        title = area.get("title", "")
        subtitle = area.get("subtitle", "")
        key_message = area.get("keyMessage", "")
        capabilities = area.get("capabilities", [])
        technologies = area.get("technologies", [])

        capabilities_text = "\n".join([f"- {cap}" for cap in capabilities])
        tech_text = ", ".join(technologies)

        content = f"""{subtitle} - {title}
{key_message}

Key capabilities:
{capabilities_text}

Core technologies: {tech_text}."""

        chunks.append({
            "id": f"expertise-{i+1}",
            "type": "expertise",
            "title": subtitle,
            "content": content
        })

    print(f"  Loaded {len(chunks)} expertise areas from expertise.js")
    return chunks


def parse_js_object(js_content: str, var_name: str) -> dict:
    """Parse a JavaScript object export into Python dict."""
    # Match: export const varName = { ... };
    pattern = rf'export\s+const\s+{var_name}\s*=\s*(\{{[^;]*?\}});'
    obj_match = re.search(pattern, js_content, re.DOTALL)
    if not obj_match:
        raise ValueError(f"Could not find exported object '{var_name}' in JS file")

    obj_str = obj_match.group(1)

    # Step 1: Replace single-quoted strings with placeholder tokens
    single_quoted = []
    def save_single_quoted(match):
        content = match.group(1)
        idx = len(single_quoted)
        single_quoted.append(content)
        return f'{{{{SINGLE_{idx}}}}}'

    obj_str = re.sub(r"'([^']*)'", save_single_quoted, obj_str)

    # Step 2: Add quotes around property names
    obj_str = re.sub(r'([{,]\s*)(\w+)(\s*:)', r'\1"\2"\3', obj_str)

    # Step 3: Remove trailing commas
    obj_str = re.sub(r',(\s*[}\]])', r'\1', obj_str)

    # Step 4: Restore single-quoted strings as double-quoted
    for idx, content in enumerate(single_quoted):
        escaped = content.replace('\\', '\\\\').replace('"', '\\"')
        obj_str = obj_str.replace(f'{{{{SINGLE_{idx}}}}}', f'"{escaped}"')

    try:
        return json.loads(obj_str)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        print(f"Problematic content: {obj_str[:500]}")
        raise


def create_bio_chunks() -> list[dict]:
    """Create text chunks from bio in expertise.js file."""
    expertise_path = Path(__file__).parent / "expertise.js"

    with open(expertise_path, "r") as f:
        js_content = f.read()

    bio_data = parse_js_object(js_content, "bio")

    name = bio_data.get("name", "")
    title = bio_data.get("title", "")
    summary = bio_data.get("summary", "")
    experience = bio_data.get("experience", "")
    competencies = bio_data.get("competencies", [])
    industries = bio_data.get("industries", [])
    philosophy = bio_data.get("philosophy", "")

    competencies_text = ", ".join(competencies)
    industries_text = ", ".join(industries)

    content = f"""About {name} - {title}.
{summary}
{experience}
Core competencies include {competencies_text}.
Industry expertise spans {industries_text} sectors.
{name}'s philosophy: {philosophy}"""

    chunks = [{
        "id": "bio-1",
        "type": "biography",
        "title": f"About {name}",
        "content": content
    }]

    print(f"  Loaded bio from expertise.js")
    return chunks


def main():
    """Generate embeddings for all portfolio data."""
    print("🚀 Starting embedding generation with Jina AI...")

    # Collect all chunks
    chunks = []
    chunks.extend(create_project_chunks())
    chunks.extend(create_skills_chunks())
    chunks.extend(create_expertise_chunks())
    chunks.extend(create_bio_chunks())

    print(f"📝 Processing {len(chunks)} chunks...")

    # Generate embeddings
    embeddings_data = []
    for i, chunk in enumerate(chunks):
        print(f"  [{i+1}/{len(chunks)}] Generating embedding for: {chunk['title']}")

        embedding = get_embedding(chunk["content"])

        embeddings_data.append({
            "id": chunk["id"],
            "type": chunk["type"],
            "title": chunk["title"],
            "content": chunk["content"],
            "embedding": embedding
        })

    # Save to JSON files (src/data and public for production)
    output_data = {
        "model": EMBEDDING_MODEL,
        "provider": "jina",
        "dimensions": len(embeddings_data[0]["embedding"]),
        "count": len(embeddings_data),
        "data": embeddings_data
    }

    # Save to src/data
    src_output_path = Path(__file__).parent / "embeddings.json"
    with open(src_output_path, "w") as f:
        json.dump(output_data, f, indent=2)

    # Save to public folder for production
    public_output_path = project_root / "public" / "embeddings.json"
    with open(public_output_path, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"\n✅ Successfully generated {len(embeddings_data)} embeddings")
    print(f"📁 Saved to:")
    print(f"   - {src_output_path}")
    print(f"   - {public_output_path}")
    print(f"📊 Embedding dimensions: {len(embeddings_data[0]['embedding'])}")


if __name__ == "__main__":
    main()
