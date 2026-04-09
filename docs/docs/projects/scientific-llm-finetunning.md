# 🧪 Scientific LLM Finetunning

A production-ready LLM engineering repository for building domain-specific assistants
(for example, scientific QA systems).

**Status**: Active &nbsp;|&nbsp; [View on GitHub](https://github.com/asierabreu/ai-nlp/tree/main/projects/scientific-llm-finetunning)

---

## Overview

This project provides an end-to-end engineering stack for domain-focused language
assistants. It includes data ingestion and normalization pipelines, configurable
GPT-style model development, pretraining and supervised fine-tuning workflows,
high-throughput inference options, a FastAPI serving layer, and production
monitoring with Prometheus, Grafana, and Weights & Biases.

---

## Highlights

- Data ingestion from JSON/text/API sources
- Cleaning, normalization, and tokenization with custom tokenizer support
- Dataset versioning with reproducible manifests
- Configurable GPT-style model settings (125M to 1B+ templates)
- RoPE-ready architecture configuration hooks
- Pretraining + SFT workflows with bf16, grad accumulation, checkpointing
- Distributed training support patterns for FSDP / DeepSpeed
- Perplexity and QA benchmark evaluation helpers
- Human evaluation export hooks
- vLLM integration path with batch/stream generation
- FastAPI endpoints: `/generate`, `/health`, `/metrics`
- Docker and optional Kubernetes deployment manifests
- Structured JSON logging and Prometheus metrics

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Data Pipeline | Python, requests, datasets |
| Models | PyTorch, Hugging Face Transformers |
| Training | Transformers Trainer, bf16, FSDP/DeepSpeed configs |
| Inference | vLLM (optional), Transformers pipeline fallback |
| Serving | FastAPI, Uvicorn |
| Monitoring | Prometheus, Grafana, Weights & Biases |
| Packaging | Docker, Docker Compose, Kubernetes manifests |

---

## Quick Start

```bash
cd projects/scientific-llm-finetunning
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run data pipeline

```bash
python scripts/run_data_pipeline.py \
  --input data/raw/sample_scientific_qa.jsonl \
  --output data/processed/scientific_qa \
  --source-type jsonl \
  --custom-tokenizer
```

### Run API

```bash
uvicorn src.serving.api:app --host 0.0.0.0 --port 8080
```

### End-to-end smoke test

```bash
python scripts/end_to_end_smoke.py \
  --input data/raw/sample_scientific_qa.jsonl \
  --output data/processed/smoke
```

---

## Serving and Monitoring

```bash
docker compose up --build
```

- API: `http://localhost:8080`
- Health: `http://localhost:8080/health`
- Metrics: `http://localhost:8080/metrics`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`

---

## Running Tests

```bash
pytest tests/ -v
```
