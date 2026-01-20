from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
import re

@dataclass
class TextPreprocessorConfig:
    lowercase: bool = True
    collapse_whitespace: bool = True
    strip: bool = True
    max_len: int = 2000
    min_len: int = 1

class TextPreprocessor:
    def __init__(self, config: TextPreprocessorConfig | None = None):
        self.config = config or TextPreprocessorConfig()

    def clean_text(self, text: str | None) -> str:
        if text is None:
            return ""

        t = str(text)

        if self.config.strip:
            t = t.strip()

        if self.config.lowercase:
            t = t.lower()

        if self.config.collapse_whitespace:
            t = re.sub(r"\s+", " ", t)

        t = t[: self.config.max_len]

        if len(t) < self.config.min_len:
            return ""

        return t

    def clean_texts(self, texts: Sequence[str | None]) -> list[str]:
        return [self.clean_text(x) for x in texts]
