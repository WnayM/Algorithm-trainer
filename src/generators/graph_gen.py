from __future__ import annotations

from random import Random 
from typing import list, Tuple

def generate_dag(n : int, edge_prob: float, seed : int | None = None ) -> tuple[list[str], list[tuple[str, str]]]:
    if n < 2:
        raise ValueError("n must be >= 2")
    if not (0.0 <= edge_prob <= 1.0):
        raise ValueError ("edge_prob must be in [0,1]")
    
    rng = Random(seed)

    nodes: list[str] = [chr(ord("A") + i) for i in range(n)]

    edges: list[tuple[str, str]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < edge_prob:
                edges.append((nodes[i], nodes[j]))
    
    if not edges:
        i = rng.randrange(0, n - 1)
        j = rng.randrange(i + 1, n)
        edges.append((nodes[i], nodes[j]))

    return nodes, edges