# 📊 NLP Knowledge Graph Extraction

Extract named entities and relationships from raw text to automatically build structured knowledge graphs using state-of-the-art NLP models.

## Overview

This project provides a pipeline for:

1. **Named Entity Recognition (NER)** – Identify entities (persons, organizations, locations, concepts) in text using spaCy and Hugging Face Transformers.
2. **Relation Extraction** – Detect semantic relationships between extracted entities.
3. **Knowledge Graph Construction** – Build a graph representation using NetworkX and persist it to Neo4j.
4. **Visualization** – Render interactive graph visualizations.

## Tech Stack

| Component | Library |
|-----------|---------|
| NLP Pipeline | spaCy 3.x, Hugging Face Transformers |
| Graph Construction | NetworkX |
| Graph Database | Neo4j 5 |
| Notebooks | Jupyter |
| Testing | pytest |

## Project Structure

```
nlp-knowledge-graph/
├── src/
│   ├── __init__.py
│   ├── ner.py              # Named entity recognition
│   ├── relation_extractor.py  # Relation extraction
│   ├── graph_builder.py    # Knowledge graph construction
│   └── neo4j_client.py     # Neo4j integration
├── notebooks/
│   ├── 01_ner_exploration.ipynb
│   └── 02_graph_construction.ipynb
├── data/
│   ├── raw/                # Raw input text files
│   └── processed/          # Processed graph exports
├── tests/
│   └── test_graph_builder.py
├── scripts/
│   ├── build_kg.py         # Build graph JSON from raw text
│   └── visualize_kg.py     # Render PNG/HTML graph visualizations
├── requirements.txt
└── README.md
```

## Installation

```bash
# From the repo root
cd projects/nlp-knowledge-graph

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Example Usage
From project folder type:
```
python scripts/build_kg.py --input data/raw/sample.txt --output data/processed/graph.json
```

## Visualize The Generated Knowledge Graph

After generating `data/processed/graph.json`, use the visualization script.

### 1. Generate Both PNG And HTML

```bash
python scripts/visualize_kg.py \
  --input data/processed/graph.json \
  --format both
```

This creates:

- `data/processed/graph.png`
- `data/processed/graph.html`

### 2. Generate Only One Format

```bash
python scripts/visualize_kg.py --input data/processed/graph.json --format png
python scripts/visualize_kg.py --input data/processed/graph.json --format html
```

### 3. Custom Output Path

```bash
python scripts/visualize_kg.py \
  --input data/processed/graph.json \
  --format html \
  --output data/processed/sample-graph.html
```

Open the interactive output in your browser:

```bash
xdg-open data/processed/graph.html
```

## Running Tests

```bash
pytest tests/ -v
```

## Related Projects

- [LLM Fine-Tuning Toolkit](../llm-fine-tuning-toolkit/) – Fine-tune LLMs for better entity extraction
- [Text-to-KG Demo](../text2kg-demo/) – End-to-end interactive demo using this pipeline
