"""Inference runtime abstraction over multiple text-generation backends.

`InferenceEngine` lazily initializes either vLLM, Hugging Face pipelines, or a
mock backend and exposes a unified generation API across them. It also includes
a simple streaming adapter that yields token-like chunks for endpoint handlers
that need incremental responses.
"""

from __future__ import annotations

from typing import Any


class InferenceEngine:
    def __init__(self, model_name: str, backend: str = "vllm") -> None:
        self.model_name = model_name
        self.backend = backend
        self._engine = None
        self._pipeline = None
        self._sampling_cls = None

    def _load(self) -> None:
        if self.backend == "mock":
            return

        if self.backend == "vllm":
            try:
                from vllm import LLM, SamplingParams

                self._engine = LLM(model=self.model_name)
                self._sampling_cls = SamplingParams
                return
            except Exception:
                self.backend = "hf"

        from transformers import pipeline

        self._pipeline = pipeline("text-generation", model=self.model_name)

    def _ensure_loaded(self) -> None:
        if self.backend == "mock":
            return
        if self.backend == "vllm" and self._engine is not None:
            return
        if self.backend == "hf" and self._pipeline is not None:
            return
        self._load()

    def generate(self, prompt: str, max_tokens: int = 128, temperature: float = 0.7) -> str:
        if self.backend == "mock":
            return f"[mock] {prompt[:max_tokens]}"

        self._ensure_loaded()

        if self.backend == "vllm" and self._engine is not None:
            params = self._sampling_cls(max_tokens=max_tokens, temperature=temperature)
            outputs = self._engine.generate([prompt], params)
            return outputs[0].outputs[0].text

        if self._pipeline is None:
            raise RuntimeError("Inference pipeline not initialized")
        result = self._pipeline(prompt, max_new_tokens=max_tokens, temperature=temperature)
        return str(result[0].get("generated_text", ""))

    def stream(self, prompt: str, max_tokens: int = 128):
        text = self.generate(prompt=prompt, max_tokens=max_tokens)
        for token in text.split():
            yield token + " "
