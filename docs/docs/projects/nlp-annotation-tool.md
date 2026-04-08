# 🏷️ NLP Annotation Tool

A web-based data annotation utility for labelling NER, relations, and text
classifications to build high-quality training datasets.

**Status**: Planned &nbsp;|&nbsp; [View on GitHub](https://github.com/asierabreu/ai-nlp/tree/main/projects/nlp-annotation-tool)

---

## Overview

A lightweight, self-hosted annotation tool designed for NLP practitioners. It
supports NER labelling, relation annotation between entities, and text classification
tasks. Built with Streamlit and FastAPI, it stores annotations in SQLite and exports
to common formats like CoNLL, JSON, and CSV for easy integration with training
pipelines.

---

## Highlights

- NER and relation annotation interface
- Text classification labelling
- Export to CoNLL, JSON, CSV formats
- Self-hosted with SQLite storage

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| UI | Streamlit |
| API | FastAPI |
| Storage | SQLite / PostgreSQL |
| Language | Python 3.10+ |

---

## Quick Start

```bash
cd projects/nlp-annotation-tool
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the annotation UI

```bash
streamlit run app/main.py
# Visit http://localhost:8501
```

### Run the backend API

```bash
uvicorn backend.main:app --reload --port 8002
# API docs: http://localhost:8002/docs
```

---

## Supported Annotation Types

| Type | Description |
|------|-------------|
| **NER** | Highlight and label named entities in text |
| **Relations** | Draw relations between annotated entities |
| **Classification** | Assign labels to entire text spans or documents |

---

## Export Formats

```bash
# Export to CoNLL format
python scripts/export.py --format conll --output data/annotations.conll

# Export to JSON
python scripts/export.py --format json --output data/annotations.json
```

---

## Running Tests

```bash
pytest tests/ -v
```
