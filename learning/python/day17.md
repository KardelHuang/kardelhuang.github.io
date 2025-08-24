---
title: Day 17 - 模組化設計與 CLI 工具封裝
parent: Python
nav_order: 17
---

# 模組化設計與 CLI 工具封裝

模組化設計後，可以透過 `argparse` 協助我們建立 CLI 的介面，讓程式啟動時跟使用者互動

- `argparse`：建立 CLI 參數解析器
- 模組化設計：拆分功能至多個 `.py` 檔案
- CLI 實作：輸入 ➜ 處理 ➜ 輸出 ➜ 美化

## 檔案結構

```
mycli/
├── main.py
├── tools/
│   ├── __init__.py
│   ├── github.py
│   ├── score.py
│   └── ui.py
```

## 使用 `argparse` 建立 CLI 介面

```python
import argparse
from tools.github import get_user_info

parser = argparse.ArgumentParser(description="GitHub CLI 工具")
parser.add_argument("username", help="GitHub 使用者名稱")
args = parser.parse_args()

info = get_user_info(args.username)
print(info)
```

## `github.py`

```python
import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return {
            "login": data["login"],
            "repos": data["public_repos"]
        }
    else:
        return {"error": "找不到使用者"}
```