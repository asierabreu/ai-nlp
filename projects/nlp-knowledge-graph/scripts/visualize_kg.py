"""Visualize a generated knowledge graph JSON as PNG and/or HTML."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

# Ensure local imports work when running this script from any working directory.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.graph_builder import import_from_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Visualize a knowledge graph JSON export.",
    )
    parser.add_argument(
        "--input",
        dest="input_path",
        type=Path,
        required=True,
        help="Path to graph JSON produced by build_kg.py.",
    )
    parser.add_argument(
        "--format",
        choices=["png", "html", "both"],
        default="both",
        help="Output format to generate (default: both).",
    )
    parser.add_argument(
        "--output",
        dest="output_path",
        type=Path,
        default=None,
        help="Optional output path. If omitted, uses data/processed/graph.png or graph.html.",
    )
    return parser.parse_args()


def load_graph(input_path: Path):
    if not input_path.exists():
        raise FileNotFoundError(f"Input graph JSON not found: {input_path}")

    data = json.loads(input_path.read_text(encoding="utf-8"))
    return import_from_json(data)


def render_png(graph, output_path: Path) -> None:
    import matplotlib.pyplot as plt
    import networkx as nx

    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw_networkx_nodes(graph, pos, node_size=900)
    nx.draw_networkx_labels(graph, pos, font_size=8)
    nx.draw_networkx_edges(graph, pos, arrows=True, width=1.2)
    edge_labels = nx.get_edge_attributes(graph, "relation")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=7)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def render_html(graph, output_path: Path) -> None:
    from pyvis.network import Network

    output_path.parent.mkdir(parents=True, exist_ok=True)

    net = Network(
        height="750px",
        width="100%",
        directed=True,
        bgcolor="#ffffff",
        font_color="#111111",
    )

    for node, attrs in graph.nodes(data=True):
        label = attrs.get("label", "entity")
        net.add_node(node, label=node, title=f"Type: {label}", group=label)

    for source, target, attrs in graph.edges(data=True):
        relation = attrs.get("relation", "related-to")
        net.add_edge(source, target, label=relation, title=relation, arrows="to")

    net.set_options(
        """
        {
          "physics": {"enabled": true, "solver": "forceAtlas2Based"},
          "edges": {"smooth": true},
          "interaction": {"hover": true, "navigationButtons": true}
        }
        """
    )
    net.save_graph(str(output_path))


def main() -> None:
    args = parse_args()
    graph = load_graph(args.input_path)

    if args.format == "png":
        output_path = args.output_path or Path("data/processed/graph.png")
        render_png(graph, output_path)
        print(f"Saved PNG graph to: {output_path}")
        return

    if args.format == "html":
        output_path = args.output_path or Path("data/processed/graph.html")
        render_html(graph, output_path)
        print(f"Saved HTML graph to: {output_path}")
        return

    png_output = Path("data/processed/graph.png")
    html_output = Path("data/processed/graph.html")
    render_png(graph, png_output)
    render_html(graph, html_output)
    print(f"Saved PNG graph to: {png_output}")
    print(f"Saved HTML graph to: {html_output}")


if __name__ == "__main__":
    main()