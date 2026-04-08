# 🔧 LLM Fine-Tuning Toolkit

A modular framework for fine-tuning large language models on custom datasets using
parameter-efficient LoRA/QLoRA techniques with experiment tracking.

**Status**: Active &nbsp;|&nbsp; [View on GitHub](https://github.com/asierabreu/ai-nlp/tree/main/projects/llm-fine-tuning-toolkit)

---

## Overview

A comprehensive toolkit that simplifies the process of fine-tuning large language
models. It provides configurable LoRA and QLoRA adapters, automatic mixed precision
training, and built-in experiment tracking via Weights & Biases. The toolkit supports
various base models from Hugging Face and includes evaluation utilities for measuring
model performance.

---

## Highlights

- LoRA and QLoRA parameter-efficient fine-tuning
- Automatic mixed precision (AMP) support
- Weights & Biases experiment tracking
- Configurable training pipelines

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Base Models | Llama, Mistral, GPT-2 |
| Fine-tuning | PEFT / LoRA / QLoRA |
| Training | PyTorch + AMP |
| Tracking | Weights & Biases |
| Hub | Hugging Face Hub |
| Language | Python 3.10+ |

---

## Quick Start

```bash
cd projects/llm-fine-tuning-toolkit
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run a fine-tuning job

```bash
python scripts/train.py --config configs/lora_config.yaml
```

---

## Pipeline Architecture

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

---

## Configuration

Training jobs are driven by YAML config files under `configs/`:

```yaml
model:
  base_model: "meta-llama/Llama-2-7b-hf"
  lora_r: 16
  lora_alpha: 32
  lora_dropout: 0.05

training:
  epochs: 3
  batch_size: 4
  learning_rate: 2e-4
  fp16: true
```

---

## Running Tests

```bash
pytest tests/ -v
```
