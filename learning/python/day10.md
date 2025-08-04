---
title: Day 10 - 錯誤處理與例外管理
parent: Python
nav_order: 10
---

# 錯誤處理與例外管理

- Python透過 `try` / `except` / `finally` 來進行錯誤處理與例外管理
- 當 `try` 段落內遇到 `raise` 時，會檢查 `except` 是否有作例外管理，有的話才執行 `except` 段落
- 最終，不管有沒有遇到錯誤或是例外，都會執行`finally`段落

## 練習

1. 建立一個 get_score() 函式，強制使用者輸入 0–100，錯誤時使用 raise
2. 用 finally 顯示「流程結束」

```python
def get_score(x):
    try:
        score = int(x)
        if score < 0 or score > 100:
            raise ValueError("無效分數")
    except ValueError as e:
        print("錯誤:", e)
    finally:
        print("流程結束")

get_score(input("分數:"))
```
