from __future__ import annotations

from src.core.preprocess import TextPreprocessor, TextPreprocessorConfig
from src.core.types import Problem, CheckResult


def make_toposort_problem() -> Problem:
    nodes = ["a", "b", "c", "d", "e"]
    edges = [
        ("a", "c"),
        ("b", "c"),
        ("c", "d"),
        ("b", "e"),
    ]

    prompt = (
        "Topological Sort (DAG)\n"
        "Vertices: A B C D E\n"
        "Directed edges:\n"
        "  A -> C\n"
        "  B -> C\n"
        "  C -> D\n"
        "  B -> E\n\n"
        "Task: Provide ANY valid topological ordering.\n"
        "Answer format: write vertices separated by spaces, e.g. 'A B C E D'\n"
    )

    expected_example = "A B C E D"

    preprocessor = TextPreprocessor(
        TextPreprocessorConfig(
            lowercase=True,
            strip=True,
            collapse_whitespace=True,
            max_len=2000,
            min_len=1,
        )
    )

    def check_fn(user_text: str) -> CheckResult:
        got_clean = preprocessor.clean_text(user_text)
        tokens = got_clean.split(" ") if got_clean else []

        node_set = set(nodes)

        if not tokens:
            return CheckResult(
                is_correct=False,
                expected=expected_example,
                got=got_clean,
                message="empty answer",
            )

        if len(tokens) != len(set(tokens)):
            return CheckResult(
                is_correct=False,
                expected=expected_example,
                got=got_clean,
                message="duplicate nodes",
            )

        token_set = set(tokens)

        missing = sorted(node_set - token_set)
        extra = sorted(token_set - node_set)

        if missing:
            return CheckResult(
                is_correct=False,
                expected=expected_example,
                got=got_clean,
                message=f"missing nodes: {' '.join(missing)}",
            )

        if extra:
            return CheckResult(
                is_correct=False,
                expected=expected_example,
                got=got_clean,
                message=f"unknown nodes: {' '.join(extra)}",
            )

        pos = {v: i for i, v in enumerate(tokens)}
        for u, v in edges:
            if pos[u] >= pos[v]:
                return CheckResult(
                    is_correct=False,
                    expected=expected_example,
                    got=got_clean,
                    message=f"order violates edge {u}->{v}",
                )

        return CheckResult(
            is_correct=True,
            expected=expected_example,
            got=got_clean,
            message="OK",
        )

    return Problem(
        prompt=prompt,
        expected=expected_example,
        check_fn=check_fn,
    )
