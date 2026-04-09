from __future__ import annotations

from typing import Any

from transformers import AutoConfig, AutoModelForCausalLM

from src.models.config import GPTModelConfig


def build_model(cfg: GPTModelConfig):
    base_cfg = AutoConfig.from_pretrained(cfg.name_or_path)
    base_cfg.vocab_size = cfg.vocab_size
    base_cfg.hidden_size = cfg.hidden_size
    base_cfg.num_attention_heads = cfg.num_attention_heads
    base_cfg.num_hidden_layers = cfg.num_hidden_layers
    base_cfg.max_position_embeddings = cfg.max_position_embeddings

    if cfg.rope_scaling_type and cfg.rope_scaling_factor:
        base_cfg.rope_scaling = {
            "type": cfg.rope_scaling_type,
            "factor": cfg.rope_scaling_factor,
        }

    return AutoModelForCausalLM.from_config(base_cfg)


def load_model_for_inference(model_name: str, dtype: str = "auto") -> Any:
    kwargs: dict[str, Any] = {"device_map": "auto"}
    if dtype in {"bfloat16", "float16", "float32"}:
        kwargs["torch_dtype"] = dtype
    return AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
