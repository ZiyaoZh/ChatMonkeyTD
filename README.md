# ChatMonkeyTD

BTD6（气球塔防6）开箱子模拟器小游戏。

输入箱子类型和箱子数量后，程序会按概率随机生成猴子掉落结果。每只猴子包含：

- 合法三路径等级组合（仅单分支有等级，如 400、020、005）
- 随机猴子种类（从固定塔池等概率抽取）

并根据箱子数量自动输出：

- 箱数 <= 50：生成拼图 + 生成 Markdown 统计
- 箱数 > 50：终端文本统计 + 生成 Markdown 统计

## 功能特性

- 按题目概率实现 5 种箱子：木头、青铜、白银、黄金、钻石
- 黄金/钻石箱支持猴子数量随机波动
- 图片按最大等级降序排列，每行最多 8 张
- 统计支持按最大等级分组
- 自动导出 Markdown 报告
- 素材命名兼容两种格式：
  - 题面格式：{path}_{species}Insta.webp
  - 当前素材格式：{path}-{species}Insta.webp

## 项目结构

```text
ChatMonkeyTD/
├── main.py
├── btd6_sim/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── simulator.py
│   ├── renderer.py
│   └── report.py
├── assets/
│   └── InstaMonkeyIcon/
└── output/
```

## 环境要求

- Python 3.10+
- Pillow

## 安装依赖

```bash
pip install pillow
```

如果你使用仓库内虚拟环境，也可以：

```bash
source .venv/bin/activate
pip install pillow
```

## 使用方法

### 基本命令

```bash
python main.py <箱子类型> <箱子数量>
```

箱子类型可选值：

- 木头
- 青铜
- 白银
- 黄金
- 钻石

### 可选参数

- --seed：随机种子（用于复现结果）
- --assets-dir：素材目录，默认 assets/InstaMonkeyIcon
- --output：拼图输出路径，默认 output/open_result.webp
- --report：统计 Markdown 输出路径，默认 output/open_result_stats.md

### 示例

1. 生成拼图与统计（箱数 <= 50）

```bash
python main.py 钻石 10 --seed 100
```

2. 仅终端统计 + Markdown 统计（箱数 > 50）

```bash
python main.py 钻石 100 --seed 100
```

3. 自定义输出路径

```bash
python main.py 黄金 30 --output output/gold.webp --report output/gold_stats.md
```

## 概率规则

| 箱子种类 | 猴子数量概率 | 猴子等级概率（每只独立） |
|---|---|---|
| 木头 | 2:100% | 1级:80%, 2级:20% |
| 青铜 | 3:100% | 1级:20%, 2级:70%, 3级:10% |
| 白银 | 3:100% | 2级:40%, 3级:55%, 4级:5% |
| 黄金 | 2:90%, 3:10% | 3级:60%, 4级:40% |
| 钻石 | 2:60%, 3:40% | 3级:35%, 4级:60%, 5级:5% |

## 输出说明

### 箱数 <= 50

- 输出拼图文件（默认 output/open_result.webp）
- 输出 Markdown 统计（默认 output/open_result_stats.md）
- 终端打印总猴子数量

### 箱数 > 50

- 终端打印按最大等级分组统计
- 输出 Markdown 统计（默认 output/open_result_stats.md）

## 常见问题

1. 报错“素材目录不存在”

请确认目录存在且路径正确，默认应为：

assets/InstaMonkeyIcon

2. 报错“未找到猴子图标”

请检查素材文件命名是否匹配任一格式：

- xxx_塔名Insta.webp
- xxx-塔名Insta.webp

3. 为什么结果每次不同

随机过程默认不固定，添加 --seed 可以复现同一结果。

## 说明

本项目为模拟器玩法实现，不依赖游戏官方接口。