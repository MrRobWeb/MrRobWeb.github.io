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
"""

import json
import os
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


def create_project_chunks() -> list[dict]:
    """Create text chunks from projects data."""
    projects = [
        {
            "id": "project-1",
            "type": "project",
            "title": "Agentic AI Platform for Travel Industry",
            "role": "Lead Architect & Project Lead",
            "industry": "Travel",
            "date": "June 2024 - Present",
            "content": """Agentic AI Platform for Travel Industry - Lead Architect & Project Lead (June 2024 - Present).
            Architected and developed a centrally managed Agentic AI platform leveraging Retrieval-Augmented Generation (RAG)
            to enable natural language itinerary creation and editing. Designed a multi-layer architecture with React/TypeScript
            frontend, FastAPI backend with Pydantic data validation, and Langgraph-orchestrated agent workflows powered by OpenAI.
            Implemented vector search capabilities using Supabase PostgreSQL and Redis-based state management for agent persistence.
            Deployed on AWS EKS with comprehensive CI/CD pipelines and observability stack.
            Technologies: TypeScript, React, MUI, Tailwind, Python, FastAPI, Pydantic, Langgraph, Langchain, OpenAI,
            Supabase, PostgreSQL, Redis, AWS, Docker, Kubernetes (EKS), Prometheus, Grafana, Sentry.
            Impact: Enabled travel consultants to build complex itineraries through conversational AI, reducing planning time by 70%."""
        },
        {
            "id": "project-2",
            "type": "project",
            "title": "Enterprise Cloud Framework Development",
            "role": "Lead Architect & Engineering Manager",
            "industry": "Cross-Industry",
            "date": "April 2022 - May 2025",
            "content": """Enterprise Cloud Framework Development - Lead Architect & Engineering Manager (April 2022 - May 2025).
            Led the design and implementation of an enterprise-grade cloud framework enabling configuration-driven pipeline orchestration.
            Architected a modular system supporting generative AI, data transformation, validation, and streaming workloads through
            declarative YAML/JSON specifications. Built and mentored a global team of 10 engineers, establishing code review standards
            and implementing semantic versioning with bi-weekly release cycles.
            Technologies: Python, JavaScript, Scala, Terraform, Docker, AWS CDK, CloudFormation, AWS Data Services, AWS DevOps Suite.
            Impact: Reduced pipeline development time by 60% and standardized cloud operations across the organization."""
        },
        {
            "id": "project-3",
            "type": "project",
            "title": "Scalable CI/CD Infrastructure",
            "role": "Lead DevOps Engineer",
            "industry": "Energy Services",
            "date": "April 2022 - May 2025",
            "content": """Scalable CI/CD Infrastructure - Lead DevOps Engineer (April 2022 - May 2025).
            Designed and delivered a "build once, deploy everywhere" CI/CD architecture supporting 100+ concurrent deployments
            for a major energy sector billing platform migration. Engineered automated infrastructure provisioning and teardown
            capabilities using Terraform and AWS native services. Integrated seamless framework updates across all deployment instances.
            Technologies: Terraform, AWS DevOps Suite, Docker, AWS CDK, Infrastructure as Code.
            Impact: Achieved 95% deployment automation, reducing manual intervention and ensuring consistent, repeatable releases."""
        },
        {
            "id": "project-4",
            "type": "project",
            "title": "Data Pipeline Configuration Platform",
            "role": "Frontend Engineer",
            "industry": "Energy Services",
            "date": "April 2022 - May 2025",
            "content": """Data Pipeline Configuration Platform - Frontend Engineer (April 2022 - May 2025).
            Architected and developed a progressive web application enabling non-technical users to configure complex data migration pipelines.
            Supported the onboarding of 100+ legal entities to a new billing platform through self-service pipeline configuration.
            Leveraged serverless architecture with AWS App Runner and DynamoDB for scalability and cost efficiency.
            Technologies: Vue 3, Vite, Tailwind CSS, AWS DynamoDB, AWS App Runner.
            Impact: Reduced pipeline configuration time from days to hours, empowering business users with direct control."""
        },
        {
            "id": "project-5",
            "type": "project",
            "title": "Custom Analytics Solutions",
            "role": "Frontend Engineer & Lead Consultant",
            "industry": "Financial Services, Healthcare",
            "date": "January 2017 - March 2022",
            "content": """Custom Analytics Solutions - Frontend Engineer & Lead Consultant (January 2017 - March 2022).
            Delivered bespoke analytics applications integrating enterprise BI platforms (Qlik, Power BI) with custom web interfaces.
            Designed intuitive user experiences combining powerful analytical capabilities with modern frontend technologies.
            Enabled stakeholders to interact with data through tailored dashboards optimized for their specific decision-making workflows.
            Technologies: Vue 3, React, Next.js, Qlik APIs, Power BI REST APIs, JavaScript, Tailwind CSS.
            Impact: Increased analytics adoption rates by 40% through improved user experience and accessibility."""
        },
        {
            "id": "project-6",
            "type": "project",
            "title": "Enterprise Data Analytics Architecture",
            "role": "Data Engineer & Lead Consultant",
            "industry": "Manufacturing, Automotive, Financial Services, Healthcare, Public Sector",
            "date": "September 2014 - March 2022",
            "content": """Enterprise Data Analytics Architecture - Data Engineer & Lead Consultant (September 2014 - March 2022).
            Led end-to-end implementation of enterprise analytics architectures for Fortune 500 clients.
            Managed full project lifecycle from infrastructure sizing and software deployment to ERP/CRM data integration
            (SAP, Microsoft Dynamics, Salesforce). Designed semantic data models and developed executive dashboards
            with role-based access controls for sensitive data.
            Technologies: Qlik, Microsoft SSAS & SSIS, Power BI, AWS, Python.
            Impact: Delivered analytics capabilities to 10,000+ end users across multiple organizations, driving data-informed decision making."""
        },
        {
            "id": "project-7",
            "type": "project",
            "title": "Data Analytics Training Program",
            "role": "Trainer",
            "industry": "Cross-Industry",
            "date": "September 2014 - March 2022",
            "content": """Data Analytics Training Program - Trainer (September 2014 - March 2022).
            Developed and delivered comprehensive training programs in data analytics and engineering for global audiences.
            Created curriculum covering dashboard design principles, data modeling fundamentals, and advanced ETL techniques.
            Conducted deep-dive technical sessions on Qlik platform administration and optimization.
            Technologies: Data Literacy, BI Design Principles, Data Modeling, ETL Best Practices, Qlik Platform.
            Impact: Trained 500+ professionals worldwide, building organizational data literacy and technical capabilities."""
        }
    ]
    return projects


def create_expertise_chunks() -> list[dict]:
    """Create text chunks from expertise/skills data."""
    expertise = [
        {
            "id": "expertise-1",
            "type": "expertise",
            "title": "Consulting / Advisory",
            "content": """Consulting and Advisory Expertise - Driving Strategic Technology Decisions.
            Robert partners with stakeholders to translate business objectives into technology roadmaps and actionable implementation strategies.
            Key capabilities:
            - Conduct technology assessments and define modernization roadmaps for enterprises
            - Advise C-level executives on data strategy, cloud adoption, and digital transformation
            - Lead vendor evaluations and technology selection for strategic initiatives
            - Deliver training programs building organizational technical capabilities
            Core skills: Strategy, Roadmapping, Stakeholder Management, Vendor Evaluation, Training, Digital Transformation, Change Management, Business Analysis."""
        },
        {
            "id": "expertise-2",
            "type": "expertise",
            "title": "Leadership",
            "content": """Leadership Expertise - Leading High-Performance Teams.
            Robert builds and mentors global engineering teams that deliver excellence through collaboration, clear standards, and continuous improvement.
            Key capabilities:
            - Build and scale distributed engineering teams across multiple time zones
            - Establish code review standards, release processes, and engineering best practices
            - Mentor engineers through technical growth paths and career development
            - Drive agile delivery with bi-weekly release cycles and semantic versioning
            Core skills: Team Building, Agile, Scrum, Code Review, Mentoring, Release Management, OKRs, Performance Management."""
        },
        {
            "id": "expertise-3",
            "type": "expertise",
            "title": "Agentic AI / Generative AI",
            "content": """Agentic AI and Generative AI Expertise - Architecting Agentic AI Solutions.
            Robert designs production-grade AI systems that transform business operations through intelligent automation and natural language interfaces.
            Key capabilities:
            - Build multi-agent workflows using Langgraph and Langchain for complex task orchestration
            - Implement RAG architectures with vector search for context-aware AI responses
            - Deploy conversational interfaces enabling natural language interaction with enterprise systems
            - Integrate LLM orchestration with existing data pipelines and business logic
            Core technologies: Langgraph, Langchain, OpenAI, RAG, Vector Search, Supabase, FastAPI, Redis."""
        },
        {
            "id": "expertise-4",
            "type": "expertise",
            "title": "Cloud Development",
            "content": """Cloud Development Expertise - Engineering Cloud-Native Platforms.
            Robert builds scalable, secure infrastructure on AWS using Infrastructure as Code principles and modern DevOps practices.
            Key capabilities:
            - Design enterprise CI/CD pipelines supporting 100+ concurrent deployments
            - Implement Infrastructure as Code with Terraform and AWS CDK
            - Architect container orchestration with Docker and Kubernetes (EKS)
            - Establish comprehensive observability with Prometheus, Grafana, and CloudWatch
            Core technologies: AWS, Terraform, Docker, Kubernetes, CDK, CloudFormation, GitHub Actions, Prometheus."""
        },
        {
            "id": "expertise-5",
            "type": "expertise",
            "title": "Fullstack Software Engineering",
            "content": """Fullstack Software Engineering Expertise - Delivering Full-Stack Applications.
            Robert develops modern web applications from concept to deployment with focus on user experience and scalable architectures.
            Key capabilities:
            - Build responsive frontends with React and Vue.js using TypeScript
            - Develop backend services with Python/FastAPI and Node.js
            - Implement serverless architectures with AWS Lambda and App Runner
            - Create progressive web applications with offline-first capabilities
            Core technologies: React, Vue.js, TypeScript, FastAPI, Node.js, Tailwind, Vite, PostgreSQL."""
        },
        {
            "id": "expertise-6",
            "type": "expertise",
            "title": "Data Engineering / Data Analytics",
            "content": """Data Engineering and Data Analytics Expertise - Transforming Data into Insights.
            Robert architects enterprise data platforms that enable data-informed decision making across organizations.
            Key capabilities:
            - Design ETL pipelines processing billions of records with Spark and AWS Glue
            - Build semantic data models and executive dashboards for stakeholders
            - Implement self-service analytics platforms with Qlik and Power BI
            - Deliver analytics capabilities to 10,000+ end users across enterprises
            Core technologies: Python, Spark, SQL, AWS Glue, Athena, Qlik, Power BI, Redshift."""
        }
    ]
    return expertise


def create_bio_chunks() -> list[dict]:
    """Create text chunks from biography data."""
    bio = [
        {
            "id": "bio-1",
            "type": "biography",
            "title": "About Robert Weber",
            "content": """About Robert Weber - Data Engineering Manager.
            Robert Weber is a Data Engineering Manager with expertise in agentic AI, cloud architecture, data platform development,
            and engineering team leadership. He delivers scalable solutions that transform how organizations leverage data for strategic decision-making.
            Robert has over 10 years of consulting experience following an academic foundation in applied quantum physics.
            Core competencies include DevOps engineering, enterprise data architecture, project delivery, and fullstack development.
            Industry expertise spans energy, human resources, automotive, aviation, retail, and pharmaceutical sectors.
            Robert's philosophy: "Learning never exhausts the mind." — Leonardo da Vinci"""
        }
    ]
    return bio


def main():
    """Generate embeddings for all portfolio data."""
    print("🚀 Starting embedding generation with Jina AI...")

    # Collect all chunks
    chunks = []
    chunks.extend(create_project_chunks())
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

    # Save to JSON file
    output_path = Path(__file__).parent / "embeddings.json"
    with open(output_path, "w") as f:
        json.dump({
            "model": EMBEDDING_MODEL,
            "provider": "jina",
            "dimensions": len(embeddings_data[0]["embedding"]),
            "count": len(embeddings_data),
            "data": embeddings_data
        }, f, indent=2)

    print(f"\n✅ Successfully generated {len(embeddings_data)} embeddings")
    print(f"📁 Saved to: {output_path}")
    print(f"📊 Embedding dimensions: {len(embeddings_data[0]['embedding'])}")


if __name__ == "__main__":
    main()
