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
    digest_short = digest[:16]  # First 16 characters of hash
    version_dir = output / "version"
    version_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "dataset_hash": digest,
        "source": source,
        "created_at": datetime.now(UTC).isoformat(),
        "num_records": str(len(records)),
    }
    manifest_path = version_dir / f"manifest_{digest_short}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return {**manifest, "digest_short": digest_short}
