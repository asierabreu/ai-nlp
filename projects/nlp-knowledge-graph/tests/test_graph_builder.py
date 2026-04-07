"""Tests for the knowledge graph builder."""

import networkx as nx
import pytest

from src.graph_builder import build_graph, export_to_json, import_from_json
from src.ner import Entity


def make_entities():
    return [
        Entity(text="Apple", label="ORG", start=0, end=5, sentence="Apple was founded by Steve Jobs."),
        Entity(text="Steve Jobs", label="PERSON", start=21, end=31, sentence="Apple was founded by Steve Jobs."),
    ]


def test_build_graph_nodes():
    entities = make_entities()
    graph = build_graph(entities)
    assert graph.number_of_nodes() == 2
    assert "Apple" in graph.nodes
    assert "Steve Jobs" in graph.nodes


def test_build_graph_with_relations():
    entities = make_entities()
    relations = [("Apple", "founded-by", "Steve Jobs")]
    graph = build_graph(entities, relations)
    assert graph.number_of_edges() == 1
    assert graph["Apple"]["Steve Jobs"]["relation"] == "founded-by"


def test_export_import_roundtrip():
    entities = make_entities()
    relations = [("Apple", "founded-by", "Steve Jobs")]
    graph = build_graph(entities, relations)
    data = export_to_json(graph)
    restored = import_from_json(data)
    assert restored.number_of_nodes() == graph.number_of_nodes()
    assert restored.number_of_edges() == graph.number_of_edges()
