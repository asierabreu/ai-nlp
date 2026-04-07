"""Knowledge graph construction using NetworkX."""

from __future__ import annotations

from typing import List, Optional, Tuple

import networkx as nx

from .ner import Entity


Relation = Tuple[str, str, str]  # (subject, predicate, object)


def build_graph(
    entities: List[Entity],
    relations: Optional[List[Relation]] = None,
) -> nx.DiGraph:
    """Build a directed knowledge graph from entities and relations.

    Args:
        entities: List of Entity objects to add as nodes.
        relations: Optional list of (subject, predicate, object) tuples.

    Returns:
        A NetworkX directed graph.
    """
    graph = nx.DiGraph()

    # Add entity nodes
    for ent in entities:
        graph.add_node(ent.text, label=ent.label, type="entity")

    # Add relation edges
    if relations:
        for subject, predicate, obj in relations:
            graph.add_edge(subject, obj, relation=predicate)

    return graph


def export_to_json(graph: nx.DiGraph) -> dict:
    """Export the graph to a JSON-serialisable dictionary."""
    return nx.node_link_data(graph)


def import_from_json(data: dict) -> nx.DiGraph:
    """Import a graph from a JSON-serialisable dictionary."""
    return nx.node_link_graph(data)
