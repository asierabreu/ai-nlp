"""Latency benchmarking helpers for inference backends.

This module runs repeated generation calls and summarizes timing distribution
with mean and P95 latency in milliseconds. It is intended for quick comparative
checks across model/back-end combinations rather than full load-testing.
"""

from __future__ import annotations

import statistics
import time

from src.inference.engine import InferenceEngine


def benchmark_latency(model_name: str, prompt: str, runs: int = 10, backend: str = "hf") -> dict[str, float]:
    engine = InferenceEngine(model_name=model_name, backend=backend)
    samples: list[float] = []

    for _ in range(runs):
        start = time.perf_counter()
        engine.generate(prompt=prompt, max_tokens=64)
        elapsed = time.perf_counter() - start
        samples.append(elapsed)

    return {
        "mean_ms": statistics.mean(samples) * 1000.0,
        "p95_ms": statistics.quantiles(samples, n=20)[-1] * 1000.0 if len(samples) > 1 else samples[0] * 1000.0,
    }
