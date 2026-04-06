from __future__ import annotations

import math
from pathlib import Path
from typing import Dict, List, Tuple

from PIL import Image, ImageOps

from .models import MonkeyDrop


def _resolve_icon_path(assets_dir: Path, drop: MonkeyDrop) -> Path:
    # 兼容题目示例格式与当前素材库连字符格式。
    candidates = [
        assets_dir / f"{drop.path_code}_{drop.species}Insta.webp",
        assets_dir / f"{drop.path_code}-{drop.species}Insta.webp",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        f"未找到猴子图标: path={drop.path_code}, species={drop.species}, assets_dir={assets_dir}"
    )


def compose_drop_image(
    drops: List[MonkeyDrop],
    assets_dir: Path,
    output_path: Path,
    max_per_row: int = 8,
    bg_color: Tuple[int, int, int] = (20, 22, 28),
) -> Path:
    if not assets_dir.exists():
        raise FileNotFoundError(f"素材目录不存在: {assets_dir}")

    ordered = sorted(drops, key=lambda d: d.max_level, reverse=True)
    if not ordered:
        raise ValueError("没有可绘制的猴子")

    icon_paths = [_resolve_icon_path(assets_dir, drop) for drop in ordered]

    cache: Dict[Path, Image.Image] = {}
    images: List[Image.Image] = []
    for path in icon_paths:
        if path not in cache:
            cache[path] = Image.open(path).convert("RGBA")
        images.append(cache[path])

    icon_w = max(img.width for img in images)
    icon_h = max(img.height for img in images)
    cols = min(max_per_row, len(images))
    rows = math.ceil(len(images) / cols)

    canvas = Image.new("RGBA", (icon_w * cols, icon_h * rows), (*bg_color, 255))

    for i, img in enumerate(images):
        row = i // cols
        col = i % cols
        x = col * icon_w
        y = row * icon_h
        if img.size != (icon_w, icon_h):
            fitted = ImageOps.pad(img, (icon_w, icon_h), color=(0, 0, 0, 0))
            canvas.paste(fitted, (x, y), fitted)
        else:
            canvas.paste(img, (x, y), img)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)

    for image in cache.values():
        image.close()

    return output_path
