from dataclasses import dataclass
from typing import Callable

@dataclass
class CheckResult:
    is_correct: bool
    expected: str
    got: str
    message: str = ""

@dataclass
class Problem:
    prompt: str
    expected: str
    check_fn: Callable[[str], CheckResult]