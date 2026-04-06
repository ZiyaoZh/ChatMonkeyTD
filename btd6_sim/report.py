from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Dict, List

from .models import MonkeyDrop


def grouped_by_level(drops: List[MonkeyDrop]) -> Dict[int, int]:
    counter = Counter(drop.max_level for drop in drops)
    return dict(sorted(counter.items(), key=lambda item: item[0], reverse=True))


def build_text_report(drops: List[MonkeyDrop]) -> str:
    lines = ["开箱结果（按最大等级分组）:"]
    grouped = grouped_by_level(drops)
    for level, count in grouped.items():
        lines.append(f"- {level}级: {count} 只")
    lines.append(f"总猴子数量: {len(drops)}")
    return "\n".join(lines)


def build_markdown_report(
    drops: List[MonkeyDrop],
    box_type: str,
    box_count: int,
    seed: int | None,
) -> str:
    grouped = grouped_by_level(drops)
    lines = [
        "# BTD6 开箱统计",
        "",
        "## 输入参数",
        f"- 箱子类型: {box_type}",
        f"- 箱子数量: {box_count}",
        f"- 随机种子: {seed if seed is not None else '未设置'}",
        "",
        "## 结果汇总（按最大等级分组）",
        "| 最大等级 | 数量 |",
        "|---|---:|",
    ]

    for level, count in grouped.items():
        lines.append(f"| {level}级 | {count} |")

    lines.extend(
        [
            "",
            f"**总猴子数量：{len(drops)}**",
        ]
    )
    return "\n".join(lines)


def write_markdown_report(markdown: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    return output_path
