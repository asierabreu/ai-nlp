# Setup Guide

This guide covers how to set up the complete AI/NLP portfolio development environment.

## Prerequisites

| Tool | Version | Installation |
|------|---------|-------------|
| Python | 3.10+ | [python.org](https://www.python.org/) |
| Node.js | 18+ | [nodejs.org](https://nodejs.org/) |
| Docker | 24+ | [docker.com](https://docker.com) |
| Git | 2.40+ | [git-scm.com](https://git-scm.com) |

---

## 1. Clone the Repository

```bash
git clone https://github.com/asierabreu/ai-nlp.git
cd ai-nlp
```

---

## 2. Portfolio Website

```bash
cd portfolio-website
npm install
npm run dev
# Open http://localhost:3000
```

---

## 3. Python Projects

Each project has its own virtual environment:

```bash
# Example: nlp-knowledge-graph
cd projects/nlp-knowledge-graph
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Repeat for each project under `projects/` and for `shared/`.

---

## 4. Docker (All Services)

To run all services with Docker Compose:

```bash
# From the repo root
docker-compose up --build
```

Services:

| Service | URL |
|---------|-----|
| Portfolio Website | http://localhost:3000 |
| Text2KG API | http://localhost:8000/docs |
| Annotation Tool | http://localhost:8001/docs |
| Neo4j Browser | http://localhost:7474 |

---

## 5. Environment Variables

Copy and edit the example env file:

```bash
cp .env.example .env
```

Key variables:

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=changeme
WANDB_API_KEY=your_wandb_key
```

---

## 6. Running Tests

```bash
# Individual project
cd projects/nlp-knowledge-graph
pytest tests/ -v

# All Python tests (from repo root)
find projects shared -name "tests" -type d | xargs -I{} sh -c 'cd {} && pytest -v'
```
