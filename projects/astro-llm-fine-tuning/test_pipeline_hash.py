#!/usr/bin/env python3
"""Quick test to verify version directory and hash-suffixed filenames are created."""

import json
import tempfile
from pathlib import Path
from src.data.pipeline import run_data_pipeline


def test_pipeline_version_directory_and_hash():
    """Test that version directory is created and files have hash suffixes."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test input
        input_file = Path(tmpdir) / "test_input.jsonl"
        input_file.write_text(
            json.dumps({"question": "What is an exoplanet?", "answer": "A planet orbiting a star."}) + "\n"
        )
        
        output_dir = Path(tmpdir) / "output"
        
        # Run pipeline
        result = run_data_pipeline(
            input_path_or_url=str(input_file),
            output_dir=str(output_dir),
            source_type="jsonl",
            tokenizer_name="gpt2",
        )
        
        print(f"✓ Pipeline executed successfully")
        print(f"  Records processed: {result['records']}")
        print(f"  Dataset path: {result['dataset_path']}")
        
        # Verify version directory exists
        version_dir = output_dir / "version"
        assert version_dir.exists(), f"❌ Version directory not found at {version_dir}"
        print(f"✓ Version directory created at {version_dir}")
        
        # Verify manifest file with hash suffix exists
        digest_short = result["manifest"]["digest_short"]
        manifest_file = version_dir / f"manifest_{digest_short}.json"
        assert manifest_file.exists(), f"❌ Manifest file not found at {manifest_file}"
        print(f"✓ Manifest file created: {manifest_file.name}")
        
        # Verify dataset file with hash suffix exists
        dataset_file = output_dir / f"dataset_{digest_short}.jsonl"
        assert dataset_file.exists(), f"❌ Dataset file not found at {dataset_file}"
        print(f"✓ Dataset file created: {dataset_file.name}")
        
        # Verify manifest content
        manifest_data = json.loads(manifest_file.read_text())
        assert "dataset_hash" in manifest_data, "❌ Missing dataset_hash in manifest"
        assert manifest_data["dataset_hash"] == result["manifest"]["dataset_hash"], "❌ Hash mismatch"
        assert len(manifest_data["dataset_hash"]) == 64, "❌ Hash should be 64 chars (SHA256)"
        print(f"✓ Manifest contains full hash (64 chars): {manifest_data['dataset_hash'][:16]}...")
        
        # Verify dataset file has content
        dataset_lines = dataset_file.read_text().strip().split("\n")
        assert len(dataset_lines) == result["records"], "❌ Record count mismatch"
        print(f"✓ Dataset file contains {len(dataset_lines)} tokenized records")
        
        # Verify content is valid JSON
        for line in dataset_lines:
            json.loads(line)  # Will raise if invalid
        print(f"✓ All dataset records are valid JSON")
        
        print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_pipeline_version_directory_and_hash()
