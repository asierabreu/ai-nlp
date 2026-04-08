"""Build a knowledge graph JSON export from a raw text file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

# Ensure local imports work when running this script from any working directory.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.graph_builder import build_graph, export_to_json
from src.ner import extract_entities
from src.relation_extractor import extract_relations


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a knowledge graph from text and export it as JSON.",
    )
    parser.add_argument(
        "--input",
        dest="input_path",
        type=Path,
        required=True,
        help="Path to the raw input text file.",
    )
    parser.add_argument(
        "--output",
        dest="output_path",
        type=Path,
        default=Path("data/processed/graph.json"),
        help="Path to write the graph JSON output (default: data/processed/graph.json).",
    )
    parser.add_argument(
        "--model",
        dest="model_name",
        default="en_core_web_sm",
        help="spaCy model name for NER (default: en_core_web_sm).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.input_path.exists():
        raise FileNotFoundError(f"Input file not found: {args.input_path}")

    text = args.input_path.read_text(encoding="utf-8")

    entities = extract_entities(text, model_name=args.model_name)
    relations = extract_relations(text, entities)
    graph = build_graph(entities, relations)

    graph_json = export_to_json(graph)
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    args.output_path.write_text(json.dumps(graph_json, indent=2), encoding="utf-8")

    print(f"Input: {args.input_path}")
    print(f"Output: {args.output_path}")
    print(f"Entities extracted: {len(entities)}")
    print(f"Relations extracted: {len(relations)}")
    print(f"Graph nodes: {graph.number_of_nodes()}")
    print(f"Graph edges: {graph.number_of_edges()}")


if __name__ == "__main__":
    main()