from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

BoxType = str


@dataclass(frozen=True)
class BoxRule:
    monkey_count_weights: List[Tuple[int, float]]
    level_weights: List[Tuple[int, float]]


BOX_RULES: Dict[BoxType, BoxRule] = {
    "木头": BoxRule(
        monkey_count_weights=[(2, 1.0)],
        level_weights=[(1, 0.80), (2, 0.20)],
    ),
    "青铜": BoxRule(
        monkey_count_weights=[(3, 1.0)],
        level_weights=[(1, 0.20), (2, 0.70), (3, 0.10)],
    ),
    "白银": BoxRule(
        monkey_count_weights=[(3, 1.0)],
        level_weights=[(2, 0.40), (3, 0.55), (4, 0.05)],
    ),
    "黄金": BoxRule(
        monkey_count_weights=[(2, 0.90), (3, 0.10)],
        level_weights=[(3, 0.60), (4, 0.40)],
    ),
    "钻石": BoxRule(
        monkey_count_weights=[(2, 0.60), (3, 0.40)],
        level_weights=[(3, 0.35), (4, 0.60), (5, 0.05)],
    ),
}

TOWER_POOL: List[str] = [
    "Alchemist",
    "BananaFarm",
    "BeastHandler",
    "BombShooter",
    "BoomerangMonkey",
    "DartMonkey",
    "DartlingGunner",
    "Desperado",
    "Druid",
    "EngineerMonkey",
    "GlueGunner",
    "HeliPilot",
    "IceMonkey",
    "Mermonkey",
    "MonkeyAce",
    "MonkeyBuccaneer",
    "MonkeySub",
    "MonkeyVillage",
    "MortarMonkey",
    "NinjaMonkey",
    "SniperMonkey",
    "SpikeFactory",
    "SuperMonkey",
    "TackShooter",
    "Wizard",
]

VALID_BOX_TYPES = tuple(BOX_RULES.keys())
