# Astro LLM Fine-Tuning

[![Astro LLM CI](https://github.com/asierabreu/ai-nlp/actions/workflows/astro-llm-fine-tuning-ci.yml/badge.svg)](https://github.com/asierabreu/ai-nlp/actions/workflows/astro-llm-fine-tuning-ci.yml)

A production-ready framework for fine-tuning domain-specific language models, with specialized support for scientific and astronomy applications. Built with PyTorch, Hugging Face, DeepSpeed, vLLM, and Weights & Biases.

## Overview

This project implements an end-to-end pipeline for:
1. **Data Ingestion & Processing** — Load scientific Q&A, research papers, or raw text from multiple sources (JSONL, text files, REST APIs)
2. **Data Cleaning & Tokenization** — Normalize records, remove duplicates, tokenize using HuggingFace tokenizers 
3. **Supervised Fine-Tuning (SFT)** — Train models on domain-specific data using distributed training (DeepSpeed/FSDP)
4. **Serving & Inference** — Deploy models via FastAPI
5. **Monitoring & Evaluation** — Track training metrics with Weights & Biases

The framework is designed for **astronomy/exoplanet domain**, but could be reused in other scientific domains by swapping datasets and configurations.

## Features

### Data Pipeline
- **Multi-source ingestion**: JSONL, raw text files, and HTTP REST APIs
- **Data processing**: Automatic cleaning, deduplication, normalization
- **Flexible tokenization**: Built-in support for HuggingFace tokenizers (GPT-2, BERT, etc.) or custom tokenizers
- **Dataset versioning**: Automatic version manifests tracking source, record counts, and checksums

### Model Training
- **Configurable architectures**: GPT-style model configs with Hugging Face + PyTorch (125M, 1B+ parameter models)
- **Training modes**: Pretraining and supervised fine-tuning (SFT) on domain-specific data
- **Performance optimizations**:
  - Mixed precision training (`bfloat16`)
  - Gradient accumulation and checkpointing for memory efficiency
  - Distributed-ready training (DeepSpeed ZeRO-2, FSDP)
- **Experiment tracking**: Weights & Biases integration for logs, metrics, checkpoints

### Evaluation & Inference
- **Evaluation metrics**: Perplexity benchmarking, QA-specific metrics (BLEU, ROUGE, exact match)
- **Inference backends**: HuggingFace + PyTorch or vLLM for high-throughput serving
- **Generation modes**: Streaming and batch generation with configurable decoding

### Serving & Monitoring
- **FastAPI REST API**: `/generate` (text generation), `/health` (health checks), `/metrics` (Prometheus metrics)
- **Containerized deployment**: Docker + Docker Compose with optional Kubernetes manifests
- **Observability**: Weights & Biases experiment tracking, Prometheus metrics, Grafana dashboards
- **Structured logging**: JSON-formatted application logs

## Project Structure

```
astro-llm-fine-tuning/
├── configs/                    # Configuration files (YAML)
│   ├── model_125m.yaml        # 125M parameter GPT-style model config
│   ├── model_1b.yaml          # 1B parameter GPT-style model config
│   ├── training_pretrain.yaml # Pretraining hyperparameters and paths
│   ├── training_sft.yaml      # SFT (supervised fine-tuning) config
│   └── deepspeed_zero2.json   # DeepSpeed ZeRO-2 distributed training config
│
├── data/
│   ├── raw/                   # Raw input data (download here or format for ingestion)
│   │   └── qa/                # QA datasets (JSONL): astro_expert_qa.jsonl
│   └── processed/             # Output from data pipeline (versioned datasets)
│       └── *_versions/        # Version manifests for each processed dataset
│
├── scripts/                   # Executable Python scripts (CLI entry points)
│   ├── download_arxiv_papers.py      # Download papers specified in paper_specs.json
│   ├── run_data_pipeline.py          # Main data ingestion-cleaning-tokenization script
│   ├── train_pretrain.py             # Pretraining entry point (loads config, trains)
│   ├── train_sft.py                  # SFT entry point (loads config, trains)
│   ├── evaluate.py                   # Compute QA metrics on predictions
│   ├── serve.py                      # FastAPI server launcher
│   ├── benchmark_latency.py          # Latency benchmarking tool
│   └── end_to_end_smoke.py           # Integration test (smoke test)
│
├── src/                       # Core Python modules (reusable library code)
│   ├── data/                  # Data processing pipeline
│   │   ├── ingestion.py       # Load data from JSONL/text/API
│   │   ├── cleaning.py        # Normalize and deduplicate records
│   │   ├── tokenization.py    # Tokenize with HF tokenizers or custom
│   │   ├── versioning.py      # Create version manifests
│   │   └── pipeline.py        # Orchestrate full pipeline
│   │
│   ├── models/                # Model architecture definitions
│   │   ├── gpt.py             # GPT-style causal language model
│   │   └── model_card.md      # Model documentation and metadata
│   │
│   ├── training/              # Training loops and utilities
│   │   ├── sft.py             # Supervised fine-tuning trainer
│   │   ├── pretrain.py        # Pretraining trainer
│   │   └── distributed.py     # DeepSpeed/FSDP utilities
│   │
│   ├── evaluation/            # Evaluation metrics and benchmarking
│   │   ├── metrics.py         # QA metrics (BLEU, ROUGE, exact match)
│   │   ├── qa_benchmark.py    # QA-specific evaluation
│   │   └── perplexity.py      # Language modeling perplexity
│   │
│   ├── inference/             # Inference backends
│   │   ├── huggingface.py     # HF + PyTorch inference
│   │   ├── vllm_backend.py    # vLLM inference (high-throughput)
│   │   └── generator.py       # Common generation interface
│   │
│   ├── serving/               # FastAPI application
│   │   └── api.py             # /generate, /health, /metrics endpoints
│   │
│   └── monitoring/            # Observability utilities
│       ├── logging.py         # Structured JSON logging
│       ├── wandb_utils.py     # Weights & Biases integration
│       └── metrics.py         # Prometheus metrics
│
├── tests/                     # Unit and integration tests
│   ├── test_data_pipeline.py  # Data processing pipeline tests
│   ├── test_perplexity.py     # Evaluation metrics tests
│   └── test_api_health.py     # FastAPI endpoint tests
│
├── infra/
│   └── k8s/                   # Kubernetes deployment manifests
│
├── prometheus/                # Prometheus monitoring config
│   └── prometheus.yml         # Scrape configs for metrics collection
│
├── grafana/                   # Grafana dashboard configs
│   └── provisioning/          # Dashboard provisioning
│
├── Dockerfile                 # Container image definition
├── docker-compose.yml         # Multi-container orchestration (API, Prometheus, Grafana)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

### Key Directories

**`configs/`** — All configuration files are YAML (training) or JSON (DeepSpeed).
- Modify `training_sft.yaml` to change learning rate, batch size, model, paths, etc.
- Model configs define architecture (vocab size, hidden dim, num layers, etc.)
- Training configs define hyperparameters and distributed training backend

**`data/raw/`** — Input data location. Expected formats:
- **JSONL**: One JSON object per line (e.g., `{"question": "...", "answer": "..."}`)
- **Text**: Raw text file (split into records by model)
- **API**: REST endpoint returning JSON list

**`data/processed/`** — Pipeline outputs. Each run creates:
- `dataset_<hash>.jsonl` — Processed and tokenized records (filename includes first 16 chars of data hash)
- `version/manifest_<hash>.json` — Metadata with full hash, source, record count, timestamp

**`src/data/`** — The data processing pipeline orchestrates:
1. **Ingestion** — Parse input format (JSONL, text, API) into list of dicts
2. **Cleaning** — Remove duplicates, normalize text, validate schema
3. **Tokenization** — Convert text to token IDs using tokenizer
4. **Versioning** — Create manifest tracking dataset lineage and stats

## Quick Start

### Installation

Clone, set up environment, and install dependencies:

```bash
cd projects/astro-llm-fine-tuning
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 1. Prepare Data

Load and process a Q&A dataset from JSONL → tokenized dataset:

```bash
python scripts/run_data_pipeline.py \
  --input data/raw/qa/astro_expert_qa.jsonl \
  --output data/processed/sft \
  --source-type jsonl \
  --tokenizer gpt2
```

**Expected files**:
- `data/processed/sft/dataset_<hash>.jsonl` — Tokenized records (filename includes first 16 chars of data hash)
- `data/processed/sft/version/manifest_<hash>.json` — Version metadata with full hash and source tracking

### 2. Train Model

Fine-tune on the processed Q&A data:

```bash
python scripts/train_sft.py \
  --config configs/training_sft.yaml
```

**Outputs** (saved to `outputs/sft/`):
- Checkpoints every 50 steps
- Final model weights
- Training logs (also in Weights & Biases if enabled)

### 3. Serve & Generate

Start the FastAPI server and test generation:

```bash
# Terminal 1: Start server
python scripts/serve.py

# Terminal 2: Test generation
curl -X POST http://localhost:8080/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is an exoplanet?", "max_tokens": 50}'
```

### 4. Docker Deployment (Optional)

Deploy API + monitoring stack:

```bash
docker compose up --build
```

- **API**: http://localhost:8080
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000

---

## Detailed Sections

### Data Pipeline

```
Input Format        Ingestion       Cleaning        Tokenization    Output
──────────────      ─────────       ────────        ────────────    ──────
JSONL {Q, A}   →  parse_jsonl() →  deduplicate() → tokenize()  →  tokens.jsonl
text (raw)     →  read_text()   →  normalize()  → tokenize()  →  tokens.jsonl
REST API /data →  fetch_api()   →  validate()   → tokenize()  →  tokens.jsonl
```

The **Data Pipeline** (`scripts/run_data_pipeline.py`) orchestrates 4 stages:

#### Stage 1: Ingestion (`--source-type`)

Loads data from multiple formats into a normalized list of dicts:

```python
# JSONL format (Q&A pairs)
python scripts/run_data_pipeline.py --input data.jsonl --source-type jsonl

# Text format (raw documents)
python scripts/run_data_pipeline.py --input data.txt --source-type text

# API format (REST endpoint returning JSON)
python scripts/run_data_pipeline.py --input http://api.example.com/data --source-type api
```

**Expected input formats**:

*JSONL* (`data.jsonl`):
```jsonl
{"question": "What is an exoplanet?", "answer": "A planet orbiting a star..."}
{"question": "How are exoplanets detected?", "answer": "Transit method, radial velocity..."}
```

*Text* (`data.txt`):
```
This is a raw text document. It can have multiple paragraphs.
The pipeline will split it into records automatically.
```

*API* (endpoint should return JSON array):
```python
GET http://api.example.com/data
# Response:
[
  {"question": "...", "answer": "..."},
  {"question": "...", "answer": "..."}
]
```

#### Stage 2: Cleaning

Normalizes records and removes duplicates:
- **Text normalization**: Lowercase, whitespace cleanup
- **Deduplication**: Remove identical records
- **Validation**: Ensure required fields present

```python
# Example: Input with duplicate
[
  {"question": "What is an exoplanet?", "answer": "A planet..."},
  {"question": "What is an exoplanet?", "answer": "A planet..."}  # Removed
]

# Output: Deduplicated
[
  {"question": "What is an exoplanet?", "answer": "A planet..."}
]
```

#### Stage 3: Tokenization

Converts text to token IDs using a HuggingFace tokenizer:

```bash
# GPT-2 tokenizer (default)
python scripts/run_data_pipeline.py --tokenizer gpt2

# Or custom tokenizer
python scripts/run_data_pipeline.py --tokenizer allenai/scibert-scivocab-uncased --custom-tokenizer
```

Each record `{"question": "...", "answer": "..."}` becomes:
```json
{
  "input_ids": [101, 2054, 2003, 1037, ...],
  "attention_mask": [1, 1, 1, 1, ...],
  "original": "What is an exoplanet?..."
}
```

#### Stage 4: Versioning & Output

Creates version metadata and writes tokenized dataset with hash-based file tracking:

**Output directory structure**:
```
data/processed/sft/
├── dataset_a1b2c3d4e5f6g7h8.jsonl    # Tokenized records (one per line), filename includes first 16 chars of data hash
└── version/
    └── manifest_a1b2c3d4e5f6g7h8.json # Metadata (timestamp, source, record_count, full hash)
```

**Example `manifest_a1b2c3d4e5f6g7h8.json`**:
```json
{
  "dataset_hash": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
  "source": "data/raw/qa/astro_expert_qa.jsonl",
  "created_at": "2024-01-15T10:30:45+00:00",
  "num_records": "100"
}
```

### Data Pipeline Command Reference

**Full signature**:
```bash
python scripts/run_data_pipeline.py \
  --input <path|url> \
  --output <directory> \
  --source-type {jsonl|text|api} \
  --tokenizer <huggingface_name> \
  [--custom-tokenizer]
```

**Common usage patterns**:

```bash
# Q&A dataset from JSONL
python scripts/run_data_pipeline.py \
  --input data/raw/qa/astro_expert_qa.jsonl \
  --output data/processed/sft \
  --source-type jsonl

# Raw text corpus for pretraining
python scripts/run_data_pipeline.py \
  --input data/raw/papers/arxiv_papers.txt \
  --output data/processed/pretrain \
  --source-type text \
  --tokenizer gpt2

# Live API endpoint (research data)
python scripts/run_data_pipeline.py \
  --input "http://api.example.com/papers" \
  --output data/processed/live_papers \
  --source-type api \
  --tokenizer gpt2

# Custom domain tokenizer
python scripts/run_data_pipeline.py \
  --input data/raw/qa/astronomy_qa.jsonl \
  --output data/processed/astronomy \
  --source-type jsonl \
  --tokenizer allenai/scibert-scivocab-uncased \
  --custom-tokenizer
```

### Related Configuration Files

The data pipeline is config-driven and integrates with training:

- **`configs/training_sft.yaml`**: Specifies `data.train_path` (where pipeline output goes)
- **`configs/model_125m.yaml`**: Defines tokenizer vocab size (must match tokenizer output)
- **`requirements.txt`**: Dependencies (transformers, torch, etc.)



## Model Configurations

Model architecture and hyperparameters are defined in YAML config files. Two pre-configured models are included:

### `configs/model_125m.yaml` — 125M Parameter Model

Small, fast model suitable for development, testing, and resource-constrained environments:

```yaml
model:
  vocab_size: 50257          # GPT-2 vocabulary size
  context_length: 2048       # Max sequence length
  embedding_dim: 768         # Hidden dimension
  num_layers: 12             # Number of transformer layers
  num_heads: 12              # Attention heads (embedding_dim % num_heads must be 0)
  dropout: 0.1               # Dropout rate
  batch_norm: false
```

### `configs/model_1b.yaml` — 1B Parameter Model

Large model for production use cases. Adjustments:
- `embedding_dim: 2048` (higher capacity)
- `num_layers: 24` (deeper network)
- `context_length: 4096` (longer context)

### Training Configurations

#### `configs/training_pretrain.yaml` — Pretraining Config

Pretraining from scratch on raw text (language modeling):

```yaml
experiment:
  name: "scientific-pretrain"
  output_dir: "outputs/pretrain"

model:
  config_file: "configs/model_125m.yaml"

data:
  train_path: "data/processed/pretrain"    # Raw text tokenized
  eval_path: "data/processed/pretrain_eval"
  max_seq_length: 2048

training:
  learning_rate: 1.0e-4                    # Higher LR for pretrain
  batch_size: 4
  gradient_accumulation_steps: 4           # Effective batch: 4 * 4 = 16
  max_steps: 10000
  warmup_steps: 1000
  eval_steps: 500
  save_steps: 500
  bf16: true                               # Mixed precision (bfloat16)
  gradient_checkpointing: true             # Save memory during backward pass
  backend: "deepspeed"                     # Use DeepSpeed for distributed training
```

#### `configs/training_sft.yaml` — Supervised Fine-Tuning Config

Fine-tuning pretrained model on domain-specific Q&A:

```yaml
experiment:
  name: "scientific-sft"
  output_dir: "outputs/sft"

model:
  config_file: "configs/model_125m.yaml"   # Load pretrained checkpoint (set in script)

data:
  train_path: "data/processed/sft"         # Q&A dataset (from data pipeline)
  eval_path: "data/processed/sft_eval"
  max_seq_length: 2048

training:
  learning_rate: 2.0e-5                    # Lower LR for fine-tuning
  batch_size: 2                            # Small batch (GPU memory)
  gradient_accumulation_steps: 8           # Effective batch: 2 * 8 = 16
  max_steps: 500                           # Shorter training than pretrain
  warmup_steps: 50
  eval_steps: 50                           # Frequent evals on domain data
  save_steps: 50
  bf16: true                               # Mixed precision
  gradient_checkpointing: true
  backend: "deepspeed"                     # DeepSpeed ZeRO-2
  deepspeed_config: "configs/deepspeed_zero2.json"  # (optional)

tracking:
  use_wandb: true                          # Log to Weights & Biases
  project: "scientific-llm-finetunning"
  entity: "your-wandb-entity"              # Set to your W&B entity
```

### DeepSpeed Configuration

**Location**: `configs/deepspeed_zero2.json`

Distributed training configuration using DeepSpeed ZeRO-2 (Zero Redundancy Optimizer):

```json
{
  "fp16": {
    "enabled": false,
    "loss_scale_window": 1000
  },
  "bfloat16": {
    "enabled": true
  },
  "zero_optimization": {
    "stage": 2,
    "offload_optimizer": {
      "device": "cpu"
    }
  },
  "gradient_accumulation_steps": 8,
  "gradient_clipping": 1.0,
  "train_batch_size": 16,
  "optimizer": {
    "type": "AdamW",
    "params": {
      "lr": 2.0e-5,
      "betas": [0.9, 0.999],
      "eps": 1.0e-8,
      "weight_decay": 0.01
    }
  }
}
```

**Key Options**:
- `bfloat16.enabled: true` — Mixed precision training
- `zero_optimization.stage: 2` — Memory-efficient optimizer state sharding
- `offload_optimizer.device: "cpu"` — Offload optimizer to CPU RAM

---

## Training Workflows

### Pretraining from Scratch

For building models from scratch on large text corpora:

```bash
# 1. Prepare raw text dataset
python scripts/run_data_pipeline.py \
  --input data/raw/papers.txt \
  --output data/processed/pretrain \
  --source-type text

# 2. Run pretraining
python scripts/train_pretrain.py \
  --config configs/training_pretrain.yaml
```

**Expected output**:
- Checkpoints saved to `outputs/pretrain/` every 500 steps
- Logs streamed to Weights & Biases
- Model weights at `outputs/pretrain/final_model/`

### Supervised Fine-Tuning (SFT)

Fine-tune a pretrained model on domain-specific Q&A:

```bash
# 1. Prepare Q&A dataset from JSONL
python scripts/run_data_pipeline.py \
  --input data/raw/qa/astro_expert_qa.jsonl \
  --output data/processed/sft \
  --source-type jsonl \
  --tokenizer gpt2

# 2. Update training config to point to processed data
# (Edit configs/training_sft.yaml: data.train_path = data/processed/sft)

# 3. Run SFT
python scripts/train_sft.py \
  --config configs/training_sft.yaml
```

**Key differences from pretraining**:
- Lower learning rate (2e-5 vs 1e-4)
- Smaller batch size & max_steps (faster convergence on domain data)
- Uses pretrained checkpoint as starting point

---

## Evaluation & Benchmarking

### QA Evaluation

Compute metrics (BLEU, ROUGE, exact match) on predictions:

```bash
python scripts/evaluate.py \
  --predictions data/processed/preds.jsonl \
  --references data/processed/refs.jsonl
```

**Input format** — `data/processed/preds.jsonl`:
```jsonl
{"prediction": "An exoplanet is a planet orbiting a star..."}
{"prediction": "Exoplanets are detected using transit photometry..."}
```

**Output**: JSON metrics
```json
{
  "bleu": 0.42,
  "rouge_1": 0.55,
  "exact_match": 0.12,
  "count": 100
}
```

### Latency Benchmarking

Measure inference latency across backends:

```bash
python scripts/benchmark_latency.py \
  --backend hf \
  --model gpt2 \
  --prompt "Explain exoplanet detection." \
  --runs 20 \
  --batch-size 1
```

**Supported backends**: `hf` (HuggingFace), `vllm` (vLLM)

---

## Serving & Deployment

### Local API Server

Run a development FastAPI server:

```bash
python scripts/serve.py
```

Defaults to `http://0.0.0.0:8080`

**Endpoints**:

- **`POST /generate`** — Generate text from prompt
  ```bash
  curl -X POST http://localhost:8080/generate \
    -H "Content-Type: application/json" \
    -d '{"prompt": "What is an exoplanet?", "max_tokens": 100}'
  ```
  Response:
  ```json
  {"generated_text": "What is an exoplanet? An exoplanet is a planet..."}
  ```

- **`GET /health`** — Health check
  ```bash
  curl http://localhost:8080/health
  ```

- **`GET /metrics`** — Prometheus metrics
  ```bash
  curl http://localhost:8080/metrics
  ```

### Docker Deployment

Multi-container deployment with monitoring:

```bash
docker compose up --build
```

**Services**:
- **API** (FastAPI): `http://localhost:8080`
- **Prometheus** (metrics): `http://localhost:9090`
- **Grafana** (dashboards): `http://localhost:3000` (admin/admin)

**Docker Compose** orchestrates:
- API container (src/serving/api.py)
- Prometheus for metrics scraping
- Grafana for visualization

### Kubernetes Deployment

Deploy to Kubernetes cluster:

```bash
kubectl apply -f infra/k8s/
```

Includes deployments for API pods, ConfigMaps for configs, and Services for networking.

---

## Integration Testing

### End-to-End Smoke Test

Validates full pipeline (ingest → train → serve):

```bash
python scripts/end_to_end_smoke.py \
  --input data/raw/sample_scientific_qa.jsonl \
  --output data/processed/smoke
```

**What it tests**:
- Data pipeline: ingestion, cleaning, tokenization, versioning
- Model training: load config, initialize model, train 1 step
- Serving: start API, call /generate endpoint
- Parsing and validation at each stage

**Use case**: Pre-deployment validation, CI/CD pipeline

---

## Advanced Usage

### Custom Tokenizers

Use domain-specific tokenizers (e.g., SciBERT):

```bash
python scripts/run_data_pipeline.py \
  --input data/raw/qa/astro_expert_qa.jsonl \
  --output data/processed/sft_scibert \
  --tokenizer allenai/scibert-scivocab-uncased \
  --custom-tokenizer
```

### Multi-GPU Training

Distributed training automatically enabled with DeepSpeed config:

```bash
# Uses all available GPUs (or set CUDA_VISIBLE_DEVICES)
python scripts/train_sft.py --config configs/training_sft.yaml
```

### Weights & Biases Integration

Track experiments and hyperparameter sweeps:

```bash
# Set W&B API key
export WANDB_API_KEY=<your-key>

# Training logs automatically sent to W&B
python scripts/train_sft.py --config configs/training_sft.yaml
```

Visit `https://wandb.ai/<entity>/<project>` to view metrics, compare runs, and debug training.

---

## Troubleshooting

### Out of Memory (OOM) Errors

If training OOMs:
1. Reduce `batch_size` in config (e.g., 2 → 1)
2. Enable `gradient_accumulation_steps` to maintain effective batch size
3. Increase `gradient_checkpointing: true`
4. Use smaller model config (125m vs 1b)

### Pipeline Hangs on API Ingestion

If `source_type: api` hangs:
1. Check endpoint URL is accessible: `curl <url>`
2. Verify endpoint returns JSON array: `[{...}, {...}]`
3. Set timeout in code if API is slow

### Weights & Biases Not Logging

If W&B integration silent:
1. Set `WANDB_API_KEY` environment variable
2. Set `use_wandb: true` in training config
3. Set `entity` and `project` in config
4. Check `wandb login` in shell

---

## Notes

- **vLLM** is optional and may require CUDA-compatible GPU.
- **DeepSpeed and FSDP** are production-ready distributed backends. Tune configs for your cluster size and hardware.
- **HuggingFace tokenizers** auto-download on first use. Ensure internet access or pre-download.
- All configs support environment variable substitution (e.g., `${DATA_PATH}` in YAML).


