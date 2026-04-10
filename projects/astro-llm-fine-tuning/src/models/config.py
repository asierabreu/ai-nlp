from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GPTModelConfig:
    name_or_path: str = "gpt2"
    vocab_size: int = 50257
    hidden_size: int = 768
    num_attention_heads: int = 12
    num_hidden_layers: int = 12
    max_position_embeddings: int = 1024
    rope_scaling_type: str | None = None
    rope_scaling_factor: float | None = None
