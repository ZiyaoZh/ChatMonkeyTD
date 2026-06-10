from __future__ import annotations

import argparse
from pathlib import Path

from btd6_sim.config import VALID_BOX_TYPES
from btd6_sim.renderer import compose_drop_image
from btd6_sim.report import build_markdown_report, build_text_report, write_markdown_report
from btd6_sim.simulator import open_boxes

MAX_BOX_COUNT = 10_000_000


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="BTD6 开箱子模拟器")
    parser.add_argument("box_type", choices=VALID_BOX_TYPES, help="箱子类型")
    parser.add_argument("box_count", type=int, help=f"箱子数量（正整数，最大 {MAX_BOX_COUNT}）")
    parser.add_argument("--seed", type=int, default=None, help="随机种子，便于复现")
    parser.add_argument(
        "--assets-dir",
        type=Path,
        default=Path("assets/InstaMonkeyIcon"),
        help="猴子图标素材目录",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/open_result.png"),
        help="拼图输出路径（仅 box_count<=50 时生效）",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("output/open_result_stats.md"),
        help="统计报告 Markdown 输出路径（所有模式均会输出）",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.box_count <= 0:
        raise SystemExit("box_count 必须是正整数")
    if args.box_count > MAX_BOX_COUNT:
        raise SystemExit(f"box_count 不能大于 {MAX_BOX_COUNT}")

    if not args.assets_dir.exists():
        raise SystemExit(f"素材目录不存在: {args.assets_dir}")

    drops = open_boxes(box_type=args.box_type, box_count=args.box_count, seed=args.seed)

    markdown = build_markdown_report(
        drops=drops,
        box_type=args.box_type,
        box_count=args.box_count,
        seed=args.seed,
    )
    report_path = write_markdown_report(markdown=markdown, output_path=args.report)

    if args.box_count <= 50:
        output_path = compose_drop_image(
            drops=drops,
            assets_dir=args.assets_dir,
            output_path=args.output,
            max_per_row=8,
        )
        print(f"已生成拼图: {output_path}")
        print(f"已生成统计: {report_path}")
        print(f"总猴子数量: {len(drops)}")
    else:
        report = build_text_report(drops)
        print(report)
        print(f"统计 Markdown 已保存: {report_path}")


if __name__ == "__main__":
    main()
