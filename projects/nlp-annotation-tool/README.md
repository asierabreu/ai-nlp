# 🏷️ NLP Annotation Tool

A web-based data annotation utility for labelling Named Entity Recognition (NER),
relations, and text classifications to build high-quality training datasets for
NLP and LLM projects.

## Overview

- **NER Annotation** – Highlight text spans and assign entity labels
- **Relation Annotation** – Draw relations between labelled entities
- **Text Classification** – Assign document-level labels
- **Dataset Export** – Export annotations in CoNLL-2003, spaCy, or JSONL format
- **Multi-user Support** – Basic authentication and session management

## Tech Stack

| Component | Technology |
|-----------|-----------|
| UI | Streamlit |
| Backend API | FastAPI |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Export | JSONL, CoNLL-2003, spaCy |

## Project Structure

```
nlp-annotation-tool/
├── app/
│   ├── streamlit_app.py    # Streamlit annotation UI
│   └── components/         # UI components
├── backend/
│   ├── main.py             # FastAPI REST API
│   ├── models.py           # Database models
│   └── crud.py             # CRUD operations
├── tests/
│   └── test_crud.py
├── requirements.txt
└── README.md
```

## Installation

```bash
cd projects/nlp-annotation-tool

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

### Streamlit UI

```bash
streamlit run app/streamlit_app.py
# Visit: http://localhost:8501
```

### FastAPI Backend

```bash
uvicorn backend.main:app --reload --port 8001
# API docs: http://localhost:8001/docs
```

## Running Tests

```bash
pytest tests/ -v
```

## Export Formats

### JSONL

```json
{"text": "Apple was founded by Steve Jobs.", "entities": [{"start": 0, "end": 5, "label": "ORG"}]}
```

### CoNLL-2003

```
Apple  B-ORG
was    O
founded O
by     O
Steve  B-PER
Jobs   I-PER
```

## Related Projects

- [NLP Knowledge Graph](../nlp-knowledge-graph/) – Use annotated data to train better NER models
- [LLM Fine-Tuning Toolkit](../llm-fine-tuning-toolkit/) – Use annotated datasets for fine-tuning
