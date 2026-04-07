# 🔧 LLM Fine-Tuning Toolkit

A modular framework and scripts for efficiently fine-tuning large language models
(Llama, Mistral, GPT-2, etc.) on custom datasets using LoRA/QLoRA parameter-efficient
techniques, with integrated experiment tracking via Weights & Biases.

## Overview

This toolkit provides:

- **LoRA/QLoRA fine-tuning** – Parameter-efficient fine-tuning with minimal GPU memory
- **Dataset utilities** – Preprocessing pipelines for instruction tuning and SFT
- **Training scripts** – Ready-to-run scripts with configurable hyperparameters
- **Experiment tracking** – Weights & Biases integration for metrics and model checkpoints
- **Evaluation** – Perplexity, ROUGE, and custom metric evaluation

## Tech Stack

| Component | Library |
|-----------|---------|
| Models | Hugging Face Transformers |
| PEFT | PEFT (LoRA, QLoRA) |
| Training | PyTorch, Accelerate |
| Tracking | Weights & Biases |
| Config | Hydra / YAML |

## Project Structure

```
llm-fine-tuning-toolkit/
├── src/
│   ├── __init__.py
│   ├── trainer.py          # Core training logic
│   ├── dataset_utils.py    # Dataset loading & preprocessing
│   └── evaluation.py       # Model evaluation utilities
├── scripts/
│   ├── train.py            # Main training entry point
│   └── evaluate.py         # Evaluation script
├── configs/
│   ├── base.yaml           # Base configuration
│   └── lora_llama.yaml     # LoRA config for Llama models
├── examples/
│   └── finetune_notebook.ipynb
├── tests/
│   └── test_dataset_utils.py
├── requirements.txt
└── README.md
```

## Installation

```bash
cd projects/llm-fine-tuning-toolkit

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

```bash
# Fine-tune with LoRA
python scripts/train.py \
  --config configs/lora_llama.yaml \
  --model_name meta-llama/Llama-3.2-1B \
  --dataset_path data/my_dataset.jsonl \
  --output_dir ./output/lora-run-1
```

Or via Python:

```python
from src.trainer import LoRATrainer
from src.dataset_utils import load_instruction_dataset

dataset = load_instruction_dataset("data/my_dataset.jsonl")
trainer = LoRATrainer(
    model_name="meta-llama/Llama-3.2-1B",
    lora_r=16,
    lora_alpha=32,
    output_dir="./output",
)
trainer.train(dataset)
```

## Configuration

Edit `configs/lora_llama.yaml` to customise training:

```yaml
model:
  name: "meta-llama/Llama-3.2-1B"
  load_in_4bit: true

lora:
  r: 16
  alpha: 32
  dropout: 0.05
  target_modules: ["q_proj", "v_proj"]

training:
  epochs: 3
  batch_size: 4
  learning_rate: 2e-4
  warmup_steps: 100
```

## Running Tests

```bash
pytest tests/ -v
```

## Related Projects

- [Domain-Specific LLM](../domain-specific-llm/) – Uses this toolkit for domain adaptation
- [NLP Knowledge Graph](../nlp-knowledge-graph/) – NLP pipeline that can be boosted with fine-tuned models
