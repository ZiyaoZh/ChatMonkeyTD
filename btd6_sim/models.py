from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class MonkeyDrop:
    species: str
    path: Tuple[int, int, int]

    @property
    def path_code(self) -> str:
        return f"{self.path[0]}{self.path[1]}{self.path[2]}"

    @property
    def max_level(self) -> int:
        return max(self.path)
