#!/usr/bin/env python3
"""Fetch exoplanet-related papers from arXiv and update paper_specs.json.

This script queries the arXiv API for papers in astro-ph.EP (exoplanet) category,
covering topics from planetary system formation to detection methods and statistical
analyses.

Output is in JSON format where each paper ID maps to a dictionary with:
  - type: "archive" or "extract" (latex handling mode)
  - title: the paper's title

Example:
    {
      "2209.15430": {
        "type": "archive",
        "title": "Linearity of Relation Decoding in Transformer Language Models"
      }
    }

Usage:
    python scripts/arxiv_papers_search.py --max-results 1000
    python scripts/arxiv_papers_search.py --max-results 500 --output data/paper_specs.json

Default behavior writes to data/paper_specs.json with up to 1000 papers.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch exoplanet papers from arXiv and update paper specs."
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=1000,
        help="Maximum number of papers to fetch (default: 1000).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/paper_specs.json"),
        help="Output JSON file path (default: data/paper_specs.json).",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="HTTP timeout in seconds (default: 60.0).",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=200,
        help="Number of results per API request (default: 200, max 200).",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=3.0,
        help="Delay between requests in seconds (default: 3.0, per arXiv API ToU).",
    )
    return parser.parse_args()


def fetch_arxiv_chunk(
    query: str, start: int, max_results: int, timeout: float
) -> bytes:
    """Fetch a chunk of results from arXiv API."""
    params = {
        "search_query": query,
        "start": str(start),
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)

    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Failed to fetch from arXiv API: {exc}") from exc


def parse_arxiv_papers(atom_response: bytes) -> list[tuple[str, str]]:
    """Parse arXiv paper IDs and titles from Atom XML response.
    
    Returns:
        List of (paper_id, title) tuples
    """
    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        root = ET.fromstring(atom_response)
    except ET.ParseError as exc:
        raise ValueError(f"Failed to parse Atom XML: {exc}") from exc

    papers: list[tuple[str, str]] = []
    for entry in root.findall("a:entry", ns):
        id_url = entry.findtext("a:id", default="", namespaces=ns).strip()
        if not id_url:
            continue

        # Extract paper ID from URL like http://arxiv.org/abs/2501.14082v1
        paper_id = id_url.rsplit("/", 1)[-1]

        # Remove version suffix (e.g., "2501.14082v1" -> "2501.14082")
        if "v" in paper_id:
            parts = paper_id.split("v")
            if len(parts) == 2 and parts[1].isdigit():
                paper_id = parts[0]

        # Extract title, removing newlines/extra whitespace
        title = entry.findtext("a:title", default="", namespaces=ns).strip()
        title = " ".join(title.split())  # Normalize whitespace

        papers.append((paper_id, title))

    return papers


def build_exoplanet_query() -> str:
    """Build search query for exoplanet-related papers in astro-ph."""
    # Primary category: astro-ph.EP (exoplanets)
    # Complementary keywords to cover various aspects of exoplanet science
    terms = [
        "cat:astro-ph.EP",  # Exoplanet primary category
        '(all:exoplanet OR all:"extrasolar planet" OR all:"planetary system")',
        '(all:formation OR all:"planet formation" OR all:protoplanetary)',
        '(all:transit OR all:"radial velocity" OR all:microlensing OR all:"direct imaging" OR all:"astrometry" OR all:"timing variations")',
        '(all:"occurrence rates" OR all:population OR all:statistics OR all:demographics)',
    ]
    return " AND ".join(terms)


def fetch_all_papers(
    query: str, max_results: int, timeout: float, chunk_size: int, delay: float
) -> list[tuple[str, str]]:
    """Fetch all paper IDs and titles matching query up to max_results.
    
    Returns:
        List of (paper_id, title) tuples
    """
    print(f"Fetching exoplanet papers from arXiv (max {max_results})...")
    print(f"Query: {query}\n")

    seen: set[str] = set()
    ordered: list[tuple[str, str]] = []

    start = 0
    chunk_size = min(chunk_size, 200)  # arXiv API max

    while len(ordered) < max_results:
        print(f"  Fetching [{start}:{start + chunk_size}]...", end=" ", flush=True)
        try:
            data = fetch_arxiv_chunk(query, start, chunk_size, timeout)
        except RuntimeError as exc:
            print(f"ERROR\n{exc}")
            break

        papers = parse_arxiv_papers(data)
        print(f"got {len(papers)} results")

        if not papers:
            print("  No more results.")
            break

        for paper_id, title in papers:
            if paper_id not in seen:
                seen.add(paper_id)
                ordered.append((paper_id, title))
                if len(ordered) >= max_results:
                    break

        start += chunk_size

        # Respect arXiv API rate limit
        if len(ordered) < max_results:
            time.sleep(delay)

    return ordered[:max_results]


def write_paper_specs(papers: list[tuple[str, str]], output_path: Path) -> None:
    """Write paper IDs, types, and titles to JSON.
    
    Output format:
    {
      "paper_id": {
        "type": "archive",
        "title": "Paper Title"
      }
    }
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Build the paper specs dictionary
    paper_specs = {}
    for paper_id, title in papers:
        paper_specs[paper_id] = {
            "type": "archive",
            "title": title,
        }
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(paper_specs, f, indent=2, ensure_ascii=True)
        f.write("\n")

    print(f"\nWrote {len(paper_specs)} papers to {output_path}")


def main() -> None:
    args = parse_args()

    query = build_exoplanet_query()
    paper_ids = fetch_all_papers(
        query,
        max_results=args.max_results,
        timeout=args.timeout,
        chunk_size=args.chunk_size,
        delay=args.delay,
    )

    write_paper_specs(paper_ids, args.output)
    print("Done.")


if __name__ == "__main__":
    main()
