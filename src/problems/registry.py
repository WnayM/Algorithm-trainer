from typing import Callable
from src.core.types import Problem

from src.problems.graphs.arrays.toposort.problem import make_toposort_problem

PROBLEM_FACTORIES: dict[str, Callable[[], Problem]] = {
    "toposort": make_toposort_problem,
}

def list_algorithms() -> list[str]:
    return sorted(PROBLEM_FACTORIES.keys())

def make_problem(algorithm: str) -> Problem:
    key = algorithm.strip().lower()
    if key not in PROBLEM_FACTORIES:
        raise KeyError(f"Unknown algorithm: {algorithm}. Available: {', '.join(list_algorithms())}")
    return PROBLEM_FACTORIES[key]()
