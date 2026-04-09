from __future__ import annotations

from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

REQUEST_COUNT = Counter("scientific_llm_requests_total", "Total number of generation requests")
REQUEST_LATENCY = Histogram("scientific_llm_request_latency_seconds", "Generation request latency")


def metrics_payload() -> tuple[bytes, str]:
    return generate_latest(), CONTENT_TYPE_LATEST
