# 🤖 AI/NLP Portfolio

A comprehensive monorepo showcasing cutting-edge work in Natural Language Processing,
Knowledge Graphs, and Large Language Model fine-tuning.

[![Website Deploy](https://github.com/asierabreu/ai-nlp/actions/workflows/website-deploy.yml/badge.svg)](https://github.com/asierabreu/ai-nlp/actions/workflows/website-deploy.yml)
[![Tests](https://github.com/asierabreu/ai-nlp/actions/workflows/tests.yml/badge.svg)](https://github.com/asierabreu/ai-nlp/actions/workflows/tests.yml)
[![Lint](https://github.com/asierabreu/ai-nlp/actions/workflows/lint.yml/badge.svg)](https://github.com/asierabreu/ai-nlp/actions/workflows/lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

## 🗂️ Repository Structure

```
ai-nlp/
├── portfolio-website/       # Modern Next.js portfolio homepage
├── projects/
│   ├── nlp-knowledge-graph/     # Knowledge graph extraction from text
│   ├── llm-fine-tuning-toolkit/ # LLM fine-tuning framework
│   ├── domain-specific-llm/     # Domain-specialized LLM
│   ├── text2kg-demo/            # Integrated text-to-KG demo
│   └── nlp-annotation-tool/     # Data annotation utility
├── shared/                  # Shared utilities and libraries
├── docs/                    # Portfolio documentation
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

- **Tech**: FastAPI, React, Neo4j, spaCy, Transformers
- **Highlights**: REST API, interactive visualization, real-time processing

---

### 5. 🏷️ [NLP Annotation Tool](./projects/nlp-annotation-tool/)

A web-based data annotation utility for labelling NER, relations, and text
classifications to build high-quality training datasets.

- **Tech**: Streamlit / FastAPI, SQLite/PostgreSQL
- **Highlights**: Annotation UI, multi-label support, dataset export

---

## ⚡ Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose (optional)

### Clone & Setup

```bash
git clone https://github.com/asierabreu/ai-nlp.git
cd ai-nlp

# Python virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Portfolio website
cd portfolio-website
npm install
npm run dev
# Visit http://localhost:3000
```

### Docker (All Services)

```bash
docker-compose up --build
```

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Frontend** | Next.js 14, React 18, TypeScript, Tailwind CSS |
| **Backend** | Python 3.10+, FastAPI |
| **NLP** | spaCy, Hugging Face Transformers, NLTK |
| **LLM** | PyTorch, LoRA/QLoRA (PEFT), Weights & Biases |
| **Graph** | NetworkX, Neo4j, D3.js |
| **Deployment** | Docker, GitHub Actions, Vercel |

---

## 📚 Documentation

- [Setup Guide](./docs/setup.md)
- [Architecture Overview](./docs/architecture.md)
- [Contributing Guidelines](./docs/contributing.md)
- [FAQ](./docs/faq.md)

---

## 🤝 Contributing

Contributions are welcome! Please read the [contributing guidelines](./docs/contributing.md)
and open an issue or pull request.

---

## 📄 License

MIT License — see [LICENSE](./LICENSE) for details.

---

## 📬 Contact

- 📧 Email: contact@example.com
- 🔗 LinkedIn: [your-linkedin](https://linkedin.com)
- 💻 GitHub: [@asierabreu](https://github.com/asierabreu)
