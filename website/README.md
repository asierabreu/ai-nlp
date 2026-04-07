# AI/NLP Portfolio Website

A modern, feature-rich portfolio landing page built with **Next.js 14**, **React 18**, **TypeScript**, **Tailwind CSS**, and **Framer Motion**.

## Features

- **Next.js 14 App Router** — Modern app directory structure with server and client components
- **Dark Mode** — System-aware theme switching with `next-themes`
- **Smooth Animations** — Framer Motion scroll-triggered animations
- **Responsive Design** — Mobile-first layout with Tailwind CSS
- **GitHub API Integration** — Live repository statistics via `/api/github`
- **SEO Optimized** — Metadata, Open Graph tags, and structured data
- **Static Site Generation** — Pre-rendered pages for fast load times
- **TypeScript** — Fully type-safe codebase

## Pages

| Route | Description |
|-------|-------------|
| `/` | Home page with Hero, featured projects, stats, and tech stack |
| `/projects` | All projects listing page |
| `/projects/[slug]` | Individual project detail pages |
| `/contact` | Contact information page |
| `/about` | About page with skills and research interests |
| `/api/github` | GitHub repository stats API route |

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **UI**: React 18 + TypeScript
- **Styling**: Tailwind CSS (custom brand palette)
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **Theme**: next-themes (dark/light mode)

## Project Structure

```
portfolio-website/
├── public/
│   └── projects-metadata.json    # Legacy project data (kept for reference)
├── src/
│   ├── app/
│   │   ├── layout.tsx            # Root layout with NavBar, Footer, ThemeProvider
│   │   ├── page.tsx              # Home page
│   │   ├── about/page.tsx        # About page
│   │   ├── contact/page.tsx      # Contact page
│   │   ├── projects/
│   │   │   ├── page.tsx          # All projects listing
│   │   │   └── [slug]/page.tsx   # Individual project pages
│   │   ├── api/github/route.ts   # GitHub API route
│   │   └── globals.css           # Global styles
│   ├── components/
│   │   ├── NavBar.tsx            # Responsive navbar with mobile menu
│   │   ├── Hero.tsx              # Animated hero section
│   │   ├── ProjectCard.tsx       # Project showcase card
│   │   ├── ProjectGrid.tsx       # Grid layout for project cards
│   │   ├── TechStack.tsx         # Tech stack section
│   │   ├── Footer.tsx            # Site footer
│   │   ├── DarkModeToggle.tsx    # Theme switcher button
│   │   ├── AnimatedSection.tsx   # Scroll animation wrapper
│   │   ├── GitHubIcon.tsx        # GitHub SVG icon
│   │   └── Providers.tsx         # ThemeProvider wrapper
│   ├── content/
│   │   └── projects.json         # Project data with descriptions
│   └── lib/
│       ├── types.ts              # TypeScript type definitions
│       └── github.ts             # GitHub API utilities
├── next.config.js
├── tailwind.config.js
├── tsconfig.json
└── package.json
```

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Development

```bash
cd portfolio-website
npm install
npm run dev
```

The app will be available at [http://localhost:3000](http://localhost:3000).

### Build

```bash
npm run build
npm run start
```

### Docker

```bash
docker build -t portfolio-website .
docker run -p 3000:3000 portfolio-website
```

### Environment Variables

Create a `.env.local` file for optional configuration:

```env
# Optional: GitHub personal access token for higher API rate limits
GITHUB_TOKEN=your_github_token
```

## Customization

### Project Data

Edit `src/content/projects.json` to update the project listings. Each project supports:

```json
{
  "id": "unique-id",
  "slug": "url-slug",
  "title": "Project Title",
  "description": "Short description for cards",
  "longDescription": "Detailed description for project page",
  "emoji": "🚀",
  "tags": ["Tag1", "Tag2"],
  "githubUrl": "https://github.com/...",
  "demoUrl": "https://...",
  "docsUrl": "https://...",
  "status": "active | wip | planned",
  "highlights": ["Feature 1", "Feature 2"]
}
```

### Brand Colors

The color palette is configured in `tailwind.config.js` under `theme.extend.colors.brand`. The default is an indigo palette.

## License

MIT
