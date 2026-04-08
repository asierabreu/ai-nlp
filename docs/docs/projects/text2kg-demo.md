# 🚀 Text-to-Knowledge Graph Demo

An end-to-end interactive demo combining NLP entity extraction with LLM-powered
enrichment to construct knowledge graphs from arbitrary text input.

**Status**: Work in Progress &nbsp;|&nbsp; [View on GitHub](https://github.com/asierabreu/ai-nlp/tree/main/projects/text2kg-demo)

---

## Overview

An interactive web application that lets users input arbitrary text and visualize
the resulting knowledge graph. The backend combines spaCy for entity extraction with
a fine-tuned LLM for relationship enrichment. The frontend provides real-time graph
visualization with zoom, pan, and node detail views.

---

## Highlights

- Real-time knowledge graph construction
- Interactive graph visualization
- LLM-powered relationship enrichment
- REST API with FastAPI

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| API | FastAPI |
| NLP | spaCy |
| LLM | Hugging Face Transformers |
| Graph DB | Neo4j |
| Language | Python 3.10+ |

---

## Quick Start

```bash
cd projects/text2kg-demo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the backend

```bash
uvicorn backend.main:app --reload --port 8001
# API docs: http://localhost:8001/docs
```

---

## Architecture

```
User Input (browser)
   │
   ▼
[FastAPI /extract endpoint]
   │
   ▼
[NLP Pipeline (spaCy)] ──► Entities + Relations
   │
   ▼
[LLM Enrichment (optional)]
   │
   ▼
[Neo4j storage]
   │
   ▼
[Graph visualization]
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/extract` | Extract entities and relations from text |
| `GET` | `/graph/{id}` | Retrieve a stored knowledge graph |
| `DELETE` | `/graph/{id}` | Delete a knowledge graph |

---

## Running Tests

```bash
pytest tests/ -v
```
