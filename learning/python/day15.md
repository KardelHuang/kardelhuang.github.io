---
title: Day 15 - 模組與套件入門
parent: Python
nav_order: 15
---

# 模組與套件入門

模組的來源有分為標準模組、自訂模組、第三方套件

## 標準模組

```python
import math
print(math.sqrt(16))  # ➜ 4.0
```

## 自訂模組

```python
# myutils.py
def greet(name):
    return f"Hello, {name}!"
```

```python
from myutils import greet
print(greet("Kardel"))
```

## 第三方套件

```bash
pip install requests
```

```python
import requests
res = requests.get("https://api.github.com")
print(res.status_code)
```

## 語法回顧

- `import 模組名`：引入整個模組
- `from 模組 import 函式`：引入特定函式
- `pip install 套件名`：安裝第三方工具
  