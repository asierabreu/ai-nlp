# AI/NLP Projects

A repository showcasing some personal work in Natural Language Processing,
Knowledge Graphs, and Large Language Model fine-tuning.

[![Deploy Docs](https://github.com/asierabreu/ai-nlp/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/asierabreu/ai-nlp/actions/workflows/deploy-docs.yml)
[![Tests](https://github.com/asierabreu/ai-nlp/actions/workflows/tests.yml/badge.svg)](https://github.com/asierabreu/ai-nlp/actions/workflows/tests.yml)
[![Lint](https://github.com/asierabreu/ai-nlp/actions/workflows/lint.yml/badge.svg)](https://github.com/asierabreu/ai-nlp/actions/workflows/lint.yml)
[![Scientific LLM CI](https://github.com/asierabreu/ai-nlp/actions/workflows/scientific-llm-finetunning-ci.yml/badge.svg)](https://github.com/asierabreu/ai-nlp/actions/workflows/scientific-llm-finetunning-ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

## 🗂️ Repository Structure

```
ai-nlp/
├── docs/                    # MkDocs documentation site
│   ├── mkdocs.yml
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docs/                # Markdown source files
├── projects/
│   ├── nlp-knowledge-graph/     # Knowledge graph extraction from text
│   ├── llm-fine-tuning-toolkit/ # LLM fine-tuning framework
│   ├── domain-specific-llm/     # Domain-specialized LLM
│   ├── text2kg-demo/            # Integrated text-to-KG demo
│   ├── nlp-annotation-tool/     # Data annotation utility
│   └── scientific-llm-finetunning/ # Production-grade domain assistant stack
├── shared/                  # Shared utilities and libraries
├── .github/workflows/       # CI/CD automation
├── docker-compose.yml       # Local development setup
└── README.md
```

---

## 🚀 Projects

### 1. 📊 [NLP Knowledge Graph Extraction](./projects/nlp-knowledge-graph/)

Extract named entities and relationships from raw text to automatically build
structured knowledge graphs using state-of-the-art NLP models.

- **Tech**: spaCy, Hugging Face Transformers, NetworkX, Neo4j
- **Highlights**: Entity recognition, relation extraction, graph visualization

---

### 2. 🔧 [LLM Fine-Tuning Toolkit](./projects/llm-fine-tuning-toolkit/)

A modular framework and set of scripts for efficiently fine-tuning large language
models (Llama, Mistral, GPT-2) on custom datasets using LoRA/QLoRA techniques.

- **Tech**: Hugging Face Transformers, PyTorch, PEFT/LoRA, Weights & Biases
- **Highlights**: Parameter-efficient fine-tuning, experiment tracking, config templates

---

### 3. 🎯 [Domain-Specific LLM](./projects/domain-specific-llm/)

A pre-trained LLM that has been specialized for a specific domain through
continued pre-training and instruction fine-tuning with rigorous evaluation.

- **Tech**: Transformers, PyTorch, domain-specific datasets, evaluation libraries
- **Highlights**: Domain adaptation, benchmark evaluation, model cards

---

### 4. 🚀 [Text-to-Knowledge Graph Demo](./projects/text2kg-demo/)

An end-to-end interactive demo combining NLP entity extraction with LLM-powered
enrichment to construct knowledge graphs from arbitrary text input.

- **Tech**: FastAPI, Neo4j, spaCy, Transformers
- **Highlights**: REST API, interactive visualization, real-time processing

---

### 5. 🏷️ [NLP Annotation Tool](./projects/nlp-annotation-tool/)

A web-based data annotation utility for labelling NER, relations, and text
classifications to build high-quality training datasets.

- **Tech**: Streamlit / FastAPI, SQLite/PostgreSQL
- **Highlights**: Annotation UI, multi-label support, dataset export

---

### 6. 🧪 [Scientific LLM Finetunning](./projects/scientific-llm-finetunning/)

A production-oriented repository for domain-specific assistant engineering with
data pipelines, scalable training, FastAPI serving, and observability tooling.

- **Tech**: PyTorch, Hugging Face, FastAPI, vLLM, DeepSpeed/FSDP, Prometheus, Grafana
- **Highlights**: Dataset versioning, configurable GPT-style configs, SFT/pretraining, latency benchmarks, CI smoke pipeline

---

## ⚡ Quick Start

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (optional)

### Clone & Setup

```bash
git clone https://github.com/asierabreu/ai-nlp.git
cd ai-nlp

# Run the documentation site locally
cd docs
pip install -r requirements.txt
mkdocs serve
# Visit http://localhost:8000
```

### Docker (All Services)

```bash
docker-compose up --build
```

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Documentation** | MkDocs, Material for MkDocs |
| **Backend** | Python 3.10+, FastAPI |
| **NLP** | spaCy, Hugging Face Transformers, NLTK |
| **LLM** | PyTorch, LoRA/QLoRA (PEFT), Weights & Biases |
| **Graph** | NetworkX, Neo4j |
| **Deployment** | Docker, GitHub Actions, GitHub Pages |

---

## 📚 Documentation

- [Setup Guide](./docs/docs/setup.md)
- [Architecture Overview](./docs/docs/architecture.md)
- [Contributing Guidelines](./docs/docs/contributing.md)

---

## 🤝 Contributing

Contributions are welcome! Please read the [contributing guidelines](./docs/docs/contributing.md)
and open an issue or pull request.

---

## 📄 License

MIT License — see [LICENSE](./LICENSE) for details.

---

## 📬 Contact

- 📧 Email: asierabreu@gmail.com
- 🔗 LinkedIn: [https://www.linkedin.com/in/asierabreu](https://linkedin.com/in/asierabreu)
- 💻 GitHub: [@asierabreu](https://github.com/asierabreu)
