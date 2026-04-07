# 🚀 Text-to-Knowledge Graph Demo

An end-to-end interactive demo that combines NLP entity extraction with
LLM-powered enrichment to construct and visualize knowledge graphs
from arbitrary text input.

## Overview

Enter any text and watch it transform into a structured knowledge graph:

1. **Input Text** → FastAPI backend receives text
2. **NLP Pipeline** → Extract entities and relations (spaCy + Transformers)
3. **LLM Enrichment** → Enrich and validate relationships using an LLM
4. **Graph Storage** → Persist the graph in Neo4j
5. **Visualization** → Interactive graph rendered in the React frontend

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend API | FastAPI |
| NLP | spaCy, Transformers |
| Graph DB | Neo4j |
| Frontend | React, D3.js |
| Containerization | Docker Compose |

## Project Structure

```
text2kg-demo/
├── backend/
│   ├── main.py             # FastAPI application
│   ├── pipeline.py         # NLP + LLM pipeline
│   ├── neo4j_client.py     # Graph database client
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   └── components/
│   └── package.json
├── pipeline/
│   └── text2kg.py          # Core pipeline logic
├── tests/
│   └── test_pipeline.py
├── requirements.txt
└── README.md
```

## Quick Start with Docker

```bash
# From repo root
docker-compose up text2kg-backend neo4j

# Visit: http://localhost:8000/docs (API docs)
# Visit: http://localhost:7474 (Neo4j browser)
```

## Manual Setup

```bash
cd projects/text2kg-demo

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start the API
uvicorn backend.main:app --reload --port 8000
```

## API Usage

```bash
curl -X POST http://localhost:8000/extract \
  -H "Content-Type: application/json" \
  -d '{"text": "Apple was founded by Steve Jobs in Cupertino."}'
```

Response:

```json
{
  "entities": [
    {"text": "Apple", "label": "ORG"},
    {"text": "Steve Jobs", "label": "PERSON"},
    {"text": "Cupertino", "label": "GPE"}
  ],
  "relations": [
    {"subject": "Apple", "predicate": "founded-by", "object": "Steve Jobs"},
    {"subject": "Apple", "predicate": "located-in", "object": "Cupertino"}
  ]
}
```

## Running Tests

```bash
pytest tests/ -v
```

## Related Projects

- [NLP Knowledge Graph](../nlp-knowledge-graph/) – Core NLP pipeline used in this demo
- [LLM Fine-Tuning Toolkit](../llm-fine-tuning-toolkit/) – Toolkit for fine-tuning the enrichment LLM
