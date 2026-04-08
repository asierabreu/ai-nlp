# 🎯 Domain-Specific LLM

A pre-trained LLM specialized for a specific domain through continued pre-training
and instruction fine-tuning with rigorous evaluation benchmarks.

**Status**: Work in Progress &nbsp;|&nbsp; [View on GitHub](https://github.com/asierabreu/ai-nlp/tree/main/projects/domain-specific-llm)

---

## Overview

This project demonstrates domain adaptation of large language models through
continued pre-training on domain-specific corpora and instruction fine-tuning. It
includes a rigorous evaluation framework with domain-specific benchmarks to measure
the quality of domain adaptation, as well as tools for comparing the specialized
model against general-purpose baselines.

---

## Highlights

- Continued pre-training on domain corpora
- Instruction fine-tuning for task alignment
- Domain-specific evaluation benchmarks
- Comparison with general-purpose models

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Base Model | Hugging Face Transformers |
| Training | PyTorch |
| Fine-tuning | PEFT / LoRA |
| Evaluation | Domain-specific benchmarks |
| Language | Python 3.10+ |

---

## Quick Start

```bash
cd projects/domain-specific-llm
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Methodology

### 1. Continued Pre-Training

```bash
python training/pretrain.py --data data/domain_corpus/ --output models/pretrained/
```

### 2. Instruction Fine-Tuning

```bash
python training/finetune.py --base models/pretrained/ --output models/finetuned/
```

### 3. Evaluation

```bash
python evaluation/evaluate.py --model models/finetuned/ --benchmarks evaluation/benchmarks/
```

---

## Running Tests

```bash
pytest tests/ -v
```
