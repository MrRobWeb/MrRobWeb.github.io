# Robert Weber Portfolio

Professional portfolio website with a McKinsey-inspired corporate design and an AI-powered Digital Twin chat feature.

## Tech Stack

- **Frontend**: Vue 3, Vite, Tailwind CSS
- **Styling**: McKinsey-inspired corporate design with dark mode support
- **Charts**: Chart.js for skill visualization
- **Icons**: FontAwesome
- **AI Features**: RAG-based Digital Twin using Jina embeddings + OpenAI
- **Contact**: Web3Forms integration
- **PWA**: Offline support with Workbox

## Features

- Light/dark mode toggle
- Responsive design
- Digital Twin AI chat (RAG with vector search)
- Functional expertise slide deck
- Projects timeline
- Skills visualization
- Contact form with captcha

## Setup

### Prerequisites

- Node.js 20+
- npm

### Environment Variables

Create a `.env` file in the project root:

```env
# Contact form (https://web3forms.com/)
VITE_WEB3FORMS_ACCESS_KEY=your_key

# Digital Twin - Embeddings (https://jina.ai/embeddings/)
JINA_API_KEY=your_jina_key
VITE_JINA_API_KEY=your_jina_key

# Digital Twin - Chat (https://platform.openai.com/)
VITE_OPENAI_API_KEY=your_openai_key
```

### Generate Embeddings

To enable the Digital Twin RAG feature:

```bash
cd src/data
pip install requests python-dotenv
python generate_embeddings.py
```

### Run Locally

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Deployment

The site auto-deploys to GitHub Pages on push to `main`. See [.github/DEPLOYMENT.md](.github/DEPLOYMENT.md) for setup instructions.

## License

MIT
