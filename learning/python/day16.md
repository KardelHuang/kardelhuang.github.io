---
title: Day 16 - 第三方套件實戰與工具整合
parent: Python
nav_order: 16
---

# 第三方套件實戰與工具整合

## 學習目標

- `pip` 安裝與套件管理
- `requests` 套件進行API呼叫
- `pandas` 套件進行資料分析
- `rich` 套件美化CLI輸出

## 安裝套件

```bash
pip install requests pandas rich
```

## 使用 `request` 呼叫 API

```python
import requests

res = requests.get("https://api.github.com/users/kardelhuang")
data = res.json()
print(data["login"], data["public_repos"])
```

## 使用 `pandas` 處理資料表

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Kardel", "老師"],
    "score": [95, 88]
})
print(df.describe())
```

## 使用 `rich` 美化 CLI 輸出

```python
from rich.console import Console
console = Console()
console.print("歡迎來到 Python 第三週!", style="bold green")
```
