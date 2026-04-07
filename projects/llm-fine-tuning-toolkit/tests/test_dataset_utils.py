"""Tests for dataset utilities."""

import json
import tempfile
from pathlib import Path

import pytest

from src.dataset_utils import format_prompt, load_instruction_dataset, split_dataset


def _write_jsonl(path: Path, samples: list) -> None:
    with path.open("w") as fh:
        for s in samples:
            fh.write(json.dumps(s) + "\n")


def test_load_instruction_dataset(tmp_path):
    samples = [
        {"instruction": "Say hello", "input": "", "output": "Hello!"},
        {"instruction": "Add 1+1", "input": "1+1", "output": "2"},
    ]
    dataset_file = tmp_path / "data.jsonl"
    _write_jsonl(dataset_file, samples)

    loaded = load_instruction_dataset(dataset_file)
    assert len(loaded) == 2
    assert loaded[0]["instruction"] == "Say hello"


def test_load_missing_file():
    with pytest.raises(FileNotFoundError):
        load_instruction_dataset("nonexistent.jsonl")


def test_format_prompt_alpaca_with_input():
    sample = {"instruction": "Translate", "input": "Hello", "output": "Hola"}
    prompt = format_prompt(sample, template="alpaca")
    assert "### Instruction:" in prompt
    assert "### Input:" in prompt
    assert "### Response:" in prompt


def test_format_prompt_alpaca_no_input():
    sample = {"instruction": "Say hi", "input": "", "output": "Hi!"}
    prompt = format_prompt(sample, template="alpaca")
    assert "### Input:" not in prompt


def test_split_dataset():
    dataset = [{"i": i} for i in range(100)]
    train, val = split_dataset(dataset, train_ratio=0.9)
    assert len(train) == 90
    assert len(val) == 10
