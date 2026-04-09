from __future__ import annotations

import hashlib
import json
from datetime import datetime, UTC
from pathlib import Path
from typing import Any


def _stable_hash(records: list[dict[str, Any]]) -> str:
    payload = json.dumps(records, sort_keys=True, ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def write_version_manifest(records: list[dict[str, Any]], output_dir: str | Path, source: str) -> dict[str, str]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    digest = _stable_hash(records)
    manifest = {
        "dataset_hash": digest,
        "source": source,
        "created_at": datetime.now(UTC).isoformat(),
        "num_records": str(len(records)),
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest
