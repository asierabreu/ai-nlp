# Architecture Overview

This document describes the design decisions and architecture of the AI/NLP portfolio monorepo.

---

## Repository Structure

The repository uses a **monorepo** layout, co-locating all related projects for:

- Shared dependency management
- Unified CI/CD pipelines
- Easier cross-project code sharing via the `shared/` package

```
ai-nlp/
├── docs/                ← MkDocs documentation site
│   ├── mkdocs.yml
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docs/            ← Markdown source files
├── projects/            ← Individual AI/NLP projects (independent venvs)
│   ├── nlp-knowledge-graph/
│   ├── llm-fine-tuning-toolkit/
│   ├── domain-specific-llm/
│   ├── text2kg-demo/
│   └── nlp-annotation-tool/
├── shared/              ← Shared Python utilities (importable)
└── .github/workflows/   ← CI/CD automation
```

---

## Data Flow

### Knowledge Graph Pipeline

```
Raw Text
   │
   ▼
[NER Model] ──► Entities
   │
   ▼
[Relation Extractor] ──► Relations
   │
   ▼
[Graph Builder (NetworkX)]
   │
   ├──► Neo4j (persistence)
   └──► Visualization (D3.js / pyvis)
```

### LLM Fine-Tuning Pipeline

```
Raw Dataset (JSONL)
   │
   ▼
[dataset_utils: load + format]
   │
   ▼
[LoRA/QLoRA Trainer (PEFT + Transformers)]
   │
   ├──► Checkpoints (HuggingFace Hub / local)
   └──► Metrics (Weights & Biases)
```

### Text-to-KG Demo (End-to-End)

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
[React + D3.js visualization]
```

---

## Technology Choices

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Documentation | MkDocs + Material | Lightweight, Python-native, built-in dark mode |
| NLP library | spaCy + Transformers | Best-in-class NER + custom model support |
| Fine-tuning method | LoRA/QLoRA | Memory-efficient, production-proven |
| Graph database | Neo4j | Industry standard for knowledge graphs |
| API framework | FastAPI | Modern, async, auto-generates OpenAPI docs |
| CI/CD | GitHub Actions | Native integration, free for public repos |

---

## Deployment

- **Documentation Site** → GitHub Pages (automatic on push to `main`)
- **Backend Services** → Docker Compose (local) or Cloud Run / Fly.io (production)
- **Neo4j** → Docker (local) or Neo4j Aura (production)
