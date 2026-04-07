# 🎯 Domain-Specific LLM

A pre-trained large language model specialized for a specific domain through
continued pre-training and instruction fine-tuning, with rigorous evaluation
against domain benchmarks.

## Overview

This project documents and provides tooling for:

1. **Continued Pre-Training** – Adapting a base LLM to domain-specific language
2. **Instruction Fine-Tuning** – Aligning the domain-adapted model with human instructions
3. **Evaluation** – Benchmarking the model on domain-specific tasks
4. **Model Card** – Documenting the model's capabilities and limitations

## Tech Stack

| Component | Library |
|-----------|---------|
| Base Model | Hugging Face Transformers |
| Training | PyTorch, Accelerate, PEFT |
| Evaluation | evaluate, lm-eval-harness |
| Experiment Tracking | Weights & Biases |

## Project Structure

```
domain-specific-llm/
├── training/
│   ├── pretrain.py         # Continued pre-training script
│   └── finetune.py         # Instruction fine-tuning script
├── data/
│   ├── raw/                # Raw domain corpus
│   └── processed/          # Tokenized and formatted data
├── models/
│   └── model_card.md       # Model card and documentation
├── evaluation/
│   ├── run_eval.py         # Run benchmark evaluations
│   └── metrics.py          # Custom domain-specific metrics
├── tests/
│   └── test_metrics.py
├── requirements.txt
└── README.md
```

## Installation

```bash
cd projects/domain-specific-llm

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

### Continued Pre-Training

```bash
python training/pretrain.py \
  --model_name gpt2 \
  --data_path data/processed/corpus.txt \
  --output_dir models/domain-pretrained \
  --epochs 3
```

### Fine-Tuning

```bash
python training/finetune.py \
  --model_name models/domain-pretrained \
  --data_path data/processed/instructions.jsonl \
  --output_dir models/domain-finetuned \
  --lora_r 16
```

### Evaluation

```bash
python evaluation/run_eval.py \
  --model_path models/domain-finetuned \
  --benchmark domain_qa
```

## Running Tests

```bash
pytest tests/ -v
```

## Related Projects

- [LLM Fine-Tuning Toolkit](../llm-fine-tuning-toolkit/) – General-purpose fine-tuning framework used here
