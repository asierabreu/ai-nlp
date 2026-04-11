# Astro LLM Fine Tuning

[![Astro LLM CI](https://github.com/asierabreu/ai-nlp/actions/workflows/astro-llm-fine-tuning-ci.yml/badge.svg)](https://github.com/asierabreu/ai-nlp/actions/workflows/astro-llm-fine-tuning-ci.yml)

Production-ready LLM for building a domain-specific assistant for specialist QA.

## Features

- Data ingestion from JSON, raw text, and HTTP APIs
- Cleaning, normalization, tokenization, and dataset versioning
- GPT-style model configs with Hugging Face + PyTorch
- Pretraining and supervised fine-tuning (SFT)
- Mixed precision (`bfloat16`), gradient accumulation, checkpointing
- Distributed-ready training hooks (FSDP / DeepSpeed)
- Perplexity and QA benchmark evaluation
- Human evaluation export hooks
- vLLM-first inference path with streaming + batch generation
- FastAPI serving with `/generate`, `/health`, `/metrics`
- Dockerized service with optional Kubernetes manifests
- Monitoring with Weights & Biases + Prometheus + Grafana
- Structured JSON logging

## Project Structure

```text
astro-llm-fine-tuning/
├── configs/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
├── src/
│   ├── data/
│   ├── models/
│   ├── training/
│   ├── evaluation/
│   ├── inference/
│   ├── serving/
│   └── monitoring/
├── tests/
├── infra/k8s/
├── prometheus/
├── grafana/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Quick Start

```bash
cd projects/astro-llm-fine-tuning
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run API locally
uvicorn src.serving.api:app --host 0.0.0.0 --port 8080
```

## Data Pipeline

```bash
python scripts/run_data_pipeline.py \
  --input data/raw/sample_scientific_qa.jsonl \
  --output data/processed/scientific_qa \
  --tokenizer gpt2
```

## End-to-End Smoke

```bash
python scripts/end_to_end_smoke.py \
  --input data/raw/sample_scientific_qa.jsonl \
  --output data/processed/smoke
```

This script validates ingestion, cleaning, tokenization, dataset versioning, and the `/generate` serving path using the mock inference backend.

## Training

```bash
# Pretraining
python scripts/train_pretrain.py \
  --config configs/training_pretrain.yaml

# SFT
python scripts/train_sft.py \
  --config configs/training_sft.yaml
```

## Evaluation

```bash
python scripts/evaluate.py --predictions data/processed/preds.jsonl --references data/processed/refs.jsonl
python scripts/benchmark_latency.py --backend hf --model gpt2 --prompt "Explain CRISPR." --runs 20
```

## Serving + Monitoring

```bash
docker compose up --build
```

- API: http://localhost:8080
- Health: http://localhost:8080/health
- Metrics: http://localhost:8080/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## Notes

- `vllm` is optional and may require CUDA-compatible environments.
- Use the included DeepSpeed and FSDP settings as baseline templates, then tune for your cluster.
