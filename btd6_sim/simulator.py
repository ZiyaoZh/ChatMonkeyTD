from __future__ import annotations

import random
from typing import List, Optional, Sequence, Tuple

from .config import BOX_RULES, TOWER_POOL
from .models import MonkeyDrop


def _weighted_choice(weighted_items: Sequence[Tuple[int, float]]) -> int:
    values = [item[0] for item in weighted_items]
    weights = [item[1] for item in weighted_items]
    return random.choices(values, weights=weights, k=1)[0]


def _build_path_from_level(level: int) -> Tuple[int, int, int]:
    branch = random.randint(0, 2)
    path = [0, 0, 0]
    path[branch] = level
    return (path[0], path[1], path[2])


def open_boxes(box_type: str, box_count: int, seed: Optional[int] = None) -> List[MonkeyDrop]:
    if box_type not in BOX_RULES:
        raise ValueError(f"不支持的箱子类型: {box_type}")
    if box_count <= 0:
        raise ValueError("box_count 必须是正整数")

    if seed is not None:
        random.seed(seed)

    rule = BOX_RULES[box_type]
    results: List[MonkeyDrop] = []

    for _ in range(box_count):
        monkey_count = _weighted_choice(rule.monkey_count_weights)
        for _ in range(monkey_count):
            max_level = _weighted_choice(rule.level_weights)
            path = _build_path_from_level(max_level)
            species = random.choice(TOWER_POOL)
            results.append(MonkeyDrop(species=species, path=path))

    return results
