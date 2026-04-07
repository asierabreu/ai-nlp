# Model Card: Domain-Specific LLM

## Model Overview

- **Base Model**: (to be specified)
- **Domain**: (to be specified)
- **Fine-Tuning Method**: Continued pre-training + LoRA instruction fine-tuning
- **License**: MIT

## Intended Use

This model is designed for domain-specific language understanding and generation tasks.
It should not be used as a general-purpose assistant.

## Training Details

| Parameter | Value |
|-----------|-------|
| Base Model | TBD |
| Training Tokens | TBD |
| LoRA Rank | 16 |
| Learning Rate | 2e-4 |
| Epochs | 3 |
| Hardware | TBD |

## Evaluation Results

| Task | Score |
|------|-------|
| Domain QA (Exact Match) | TBD |
| Domain QA (F1) | TBD |
| Perplexity | TBD |

## Limitations

- Specialized for one domain; may underperform on general tasks
- Not tested for safety or bias beyond the training domain
- Hallucinations are possible

## Citation

```
@misc{domain-specific-llm-2024,
  title  = {Domain-Specific LLM},
  author = {asierabreu},
  year   = {2024},
  url    = {https://github.com/asierabreu/ai-nlp/tree/main/projects/domain-specific-llm}
}
```
