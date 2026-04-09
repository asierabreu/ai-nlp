from __future__ import annotations

from typing import Any

from transformers import AutoTokenizer, PreTrainedTokenizerBase


class WhitespaceTokenizer:
    def encode(self, text: str) -> list[int]:
        return [len(tok) for tok in text.split()]


def get_tokenizer(tokenizer_name: str = "gpt2", custom: bool = False) -> Any:
    if custom:
        return WhitespaceTokenizer()
    return AutoTokenizer.from_pretrained(tokenizer_name)


def tokenize_records(
    records: list[dict[str, Any]],
    tokenizer: PreTrainedTokenizerBase | WhitespaceTokenizer,
    text_key: str = "text",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for record in records:
        data = dict(record)
        text = str(data.get(text_key, ""))
        if hasattr(tokenizer, "encode"):
            data["input_ids"] = tokenizer.encode(text)
        else:
            data["input_ids"] = []
        out.append(data)
    return out
