from __future__ import annotations

from typing import Any


def build_training_args_backend(backend: str, deepspeed_config: str | None = None) -> dict[str, Any]:
    backend = backend.lower().strip()
    if backend == "deepspeed":
        if not deepspeed_config:
            raise ValueError("deepspeed backend requires deepspeed_config")
        return {"deepspeed": deepspeed_config}
    if backend == "fsdp":
        return {
            "fsdp": "full_shard auto_wrap",
            "fsdp_transformer_layer_cls_to_wrap": "GPT2Block",
        }
    if backend == "single":
        return {}
    raise ValueError("backend must be one of: deepspeed, fsdp, single")
