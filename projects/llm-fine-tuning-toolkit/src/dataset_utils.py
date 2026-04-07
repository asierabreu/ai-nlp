"""Dataset loading and preprocessing utilities for LLM fine-tuning."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List


def load_instruction_dataset(path: str | Path) -> List[Dict[str, str]]:
    """Load an instruction-tuning dataset from a JSONL file.

    Expected format per line:
        {"instruction": "...", "input": "...", "output": "..."}

    Args:
        path: Path to the JSONL file.

    Returns:
        List of sample dictionaries.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    samples: List[Dict[str, str]] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                samples.append(json.loads(line))

    return samples


def format_prompt(
    sample: Dict[str, str],
    template: str = "alpaca",
) -> str:
    """Format a sample dictionary into a prompt string.

    Args:
        sample: Dictionary with keys 'instruction', 'input', 'output'.
        template: Prompt template style ('alpaca' or 'simple').

    Returns:
        Formatted prompt string.
    """
    if template == "alpaca":
        if sample.get("input"):
            return (
                f"### Instruction:\n{sample['instruction']}\n\n"
                f"### Input:\n{sample['input']}\n\n"
                f"### Response:\n{sample['output']}"
            )
        return (
            f"### Instruction:\n{sample['instruction']}\n\n"
            f"### Response:\n{sample['output']}"
        )

    # simple template
    return f"User: {sample['instruction']}\nAssistant: {sample['output']}"


def split_dataset(
    dataset: List[Dict],
    train_ratio: float = 0.9,
) -> tuple[List[Dict], List[Dict]]:
    """Split dataset into train and validation sets.

    Args:
        dataset: Full dataset list.
        train_ratio: Proportion to use for training.

    Returns:
        Tuple of (train_set, val_set).
    """
    split_idx = int(len(dataset) * train_ratio)
    return dataset[:split_idx], dataset[split_idx:]
