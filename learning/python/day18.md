---
title: Day 18 - 模組測試與錯誤處理強化
parent: Python
nav_order: 18
---

# 模組測試與錯誤處理強化

- 使用 `try/except` 處理例外狀況
- 使用 `assert` 進行邏輯驗證

## 錯誤處理 `try/except`

```python
try:
    x = int(input("請輸入數字："))
    print(100 / x)
except ValueError:
    print("請輸入有效的數字")
except ZeroDivisionError:
    print("不能除以 0")
```

## 測試函式 `assert`

```python
def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("add() 測試通過")

test_add()
```
