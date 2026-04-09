# Projects Overview

This repository contains six interconnected AI/NLP projects, all written in Python
and sharing a common `shared/` utilities library.

---

## 📊 NLP Knowledge Graph Extraction

Extract named entities and relationships from raw text to automatically build
structured knowledge graphs using state-of-the-art NLP models.

- **Tech**: spaCy, Hugging Face Transformers, NetworkX, Neo4j
- **Highlights**: Entity recognition, relation extraction, graph visualization
- **Status**: Active
- **[View Project →](projects/nlp-knowledge-graph.md)**

---

## 🔧 LLM Fine-Tuning Toolkit

A modular framework and set of scripts for efficiently fine-tuning large language
models (Llama, Mistral, GPT-2) on custom datasets using LoRA/QLoRA techniques.

- **Tech**: Hugging Face Transformers, PyTorch, PEFT/LoRA, Weights & Biases
- **Highlights**: Parameter-efficient fine-tuning, experiment tracking, config templates
- **Status**: Active
- **[View Project →](projects/llm-fine-tuning-toolkit.md)**

---

## 🎯 Domain-Specific LLM

A pre-trained LLM that has been specialized for a specific domain through
continued pre-training and instruction fine-tuning with rigorous evaluation.

- **Tech**: Transformers, PyTorch, domain-specific datasets, evaluation libraries
- **Highlights**: Domain adaptation, benchmark evaluation, model cards
- **Status**: Work in Progress
- **[View Project →](projects/domain-specific-llm.md)**

---

## 🧪 Scientific LLM Finetunning

A production-ready LLM engineering stack for domain-specific assistants with
data pipelines, configurable GPT-style model setups, scalable training, serving,
and observability for real-world deployment.

- **Tech**: PyTorch, Hugging Face, FastAPI, vLLM, DeepSpeed/FSDP, Prometheus, Grafana
- **Highlights**: Dataset versioning, SFT + pretraining workflows, latency benchmarking
- **Status**: Active
- **[View Project →](projects/scientific-llm-finetunning.md)**

---

## 🚀 Text-to-Knowledge Graph Demo

An end-to-end interactive demo combining NLP entity extraction with LLM-powered
enrichment to construct knowledge graphs from arbitrary text input.

- **Tech**: FastAPI, Neo4j, spaCy, Transformers
- **Highlights**: REST API, interactive visualization, real-time processing
- **Status**: Work in Progress
- **[View Project →](projects/text2kg-demo.md)**

---

## 🏷️ NLP Annotation Tool

A web-based data annotation utility for labelling NER, relations, and text
classifications to build high-quality training datasets.

- **Tech**: Streamlit / FastAPI, SQLite/PostgreSQL
- **Highlights**: Annotation UI, multi-label support, dataset export
- **Status**: Planned
- **[View Project →](projects/nlp-annotation-tool.md)**
