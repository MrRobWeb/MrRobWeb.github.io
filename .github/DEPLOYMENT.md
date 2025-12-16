# GitHub Pages Deployment Guide

This document outlines the setup and deployment process for the portfolio site.

## Prerequisites

- Repository must be named `<username>.github.io` for user site, or any name for project site
- Node.js 20+ for local development

## GitHub Setup

### 1. Enable GitHub Pages

1. Navigate to repository **Settings**
2. Select **Pages** in the left sidebar
3. Under **Source**, select **GitHub Actions**

### 2. Configure Repository Secrets

For features like the Digital Twin chat, you need to set up environment secrets:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add the following secrets:

| Secret Name | Description |
|-------------|-------------|
| `VITE_JINA_API_KEY` | Jina AI API key for embeddings (free at https://jina.ai/embeddings/) |
| `VITE_OPENAI_API_KEY` | OpenAI API key for Digital Twin chat (https://platform.openai.com/api-keys) |

**To add a secret:**
1. Click **New repository secret**
2. Enter the **Name** (e.g., `VITE_OPENAI_API_KEY`)
3. Enter the **Secret** value (your actual API key)
4. Click **Add secret**

### 3. Configure Workflow Permissions

1. Go to **Settings** → **Actions** → **General**
2. Scroll to **Workflow permissions**
3. Select **Read and write permissions**
4. Enable **Allow GitHub Actions to create and approve pull requests**
5. Click **Save**

## Deployment

### Automatic Deployment

The site deploys automatically when pushing to the `main` branch. The workflow:

1. Checks out the code
2. Sets up Node.js 20 with npm caching
3. Installs dependencies via `npm ci`
4. Runs tests via `npm run test:run`
5. Builds the production bundle via `npm run build`
6. Uploads the `dist` folder as an artifact
7. Deploys to GitHub Pages

### Manual Deployment

To trigger a manual deployment:

1. Go to the **Actions** tab
2. Select **Deploy to GitHub Pages** workflow
3. Click **Run workflow**
4. Select the `main` branch
5. Click **Run workflow**

## Monitoring

### View Deployment Status

1. Navigate to the **Actions** tab
2. Click on the latest workflow run
3. View build and deploy job status

### View Live Site

After successful deployment, the site is available at:

```
https://<username>.github.io
```

## Troubleshooting

### Build Failures

- Check the Actions log for error details
- Ensure all dependencies are listed in `package.json`
- Verify `npm run build` works locally

### 404 Errors After Deployment

- Confirm GitHub Pages source is set to **GitHub Actions**
- Check that `dist` folder contains `index.html`
- For SPA routing, ensure proper base path configuration in `vite.config.js`

### Permission Errors

- Verify workflow permissions are set to **Read and write**
- Ensure `id-token: write` permission is in the workflow file

## Local Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Run tests
npm run test:run

# Build for production
npm run build

# Preview production build
npm run preview
```
