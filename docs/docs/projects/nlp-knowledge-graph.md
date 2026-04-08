# 📊 NLP Knowledge Graph Extraction

Extract named entities and relationships from raw text to automatically build
structured knowledge graphs using state-of-the-art NLP models.

**Status**: Active &nbsp;|&nbsp; [View on GitHub](https://github.com/asierabreu/ai-nlp/tree/main/projects/nlp-knowledge-graph)

---

## Overview

This project implements an automated pipeline for extracting structured knowledge
from unstructured text. It uses spaCy and Hugging Face Transformers for named entity
recognition and relation extraction, then stores the resulting knowledge graph in
Neo4j for efficient querying and visualization. The system supports multiple text
formats and can process large corpora in batch mode.

---

## Highlights

- Named Entity Recognition (NER) with spaCy
- Relation extraction using Transformers
- Graph storage with Neo4j
- Interactive visualization with NetworkX

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| NER | spaCy |
| Relation Extraction | Hugging Face Transformers |
| Graph Storage | Neo4j |
| Graph Analysis | NetworkX |
| Language | Python 3.10+ |

---

## Quick Start

```bash
cd projects/nlp-knowledge-graph
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## Pipeline Architecture

```
Raw Text
   │
   ▼
[NER Model (spaCy)] ──► Entities
   │
   ▼
[Relation Extractor (Transformers)] ──► Relations
   │
   ▼
[Graph Builder (NetworkX)]
   │
   ├──► Neo4j (persistence)
   └──► Visualization (pyvis)
```

---

## Running Tests

```bash
pytest tests/ -v
```
