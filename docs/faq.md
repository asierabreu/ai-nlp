# Frequently Asked Questions

## General

**Q: Why a monorepo instead of separate repositories?**  
A: A monorepo simplifies sharing code (via `shared/`), enables unified CI/CD, and makes it easier to understand the full portfolio at a glance. For a personal portfolio of related projects it's the ideal choice.

**Q: Can I use individual projects independently?**  
A: Yes! Each project under `projects/` is self-contained with its own `requirements.txt` and `README.md`. You can clone the repo and work on any single project without needing the others.

---

## Portfolio Website

**Q: How do I add a new project to the website?**  
A: Edit `portfolio-website/public/projects-metadata.json`. Add an entry with the required fields (`id`, `title`, `description`, `emoji`, `tags`, `githubUrl`, `status`). The grid will update automatically.

**Q: How do I deploy the website?**  
A: Connect the repository to [Vercel](https://vercel.com), set the root directory to `portfolio-website/`, and configure the `VERCEL_TOKEN`, `VERCEL_ORG_ID`, and `VERCEL_PROJECT_ID` secrets in your GitHub repository settings.

---

## Python Projects

**Q: Which Python version is required?**  
A: Python 3.10 or higher. Python 3.11 is recommended.

**Q: Do I need a GPU to run the LLM projects?**  
A: A GPU is strongly recommended for training. For inference with smaller models (≤ 7B parameters), a modern CPU or Apple Silicon Mac is sufficient with 4-bit quantisation.

**Q: How do I use the shared utilities in my project?**  
A: Add the repo root to your `PYTHONPATH`:
```bash
export PYTHONPATH=/path/to/ai-nlp:$PYTHONPATH
from shared.utils.text import clean_text
```

---

## CI/CD

**Q: Why are the GitHub Actions workflows failing?**  
A: Common causes:
- Missing secrets (e.g., `VERCEL_TOKEN`)
- Python dependency conflicts — check `requirements.txt` versions
- spaCy model not downloaded — the workflows install models explicitly

**Q: How do I run the CI checks locally?**  
A: Install the tools and run:
```bash
# Python
pip install ruff black isort pytest
ruff check projects/ shared/
pytest projects/nlp-knowledge-graph/tests/ -v

# JavaScript
cd portfolio-website && npm run lint && npm run build
```
