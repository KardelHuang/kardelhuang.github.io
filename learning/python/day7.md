---
title: Day 7 - 迴圈結構
parent: Python
nav_order: 7
---

# 迴圈結構

## 迴圈類型

- `for` 迴圈，將清單依序走訪即完成，會搭配 `range` 或 `list` 控制清單範圍
- `while` 迴圈，當條件式滿足時會繼續執行，直到條件不滿足

## 流程控制

- `break` 可用來跳出迴圈
- `continue` 會跳過當次，繼續下一輪

## 練習

1. 使用 `for` 印出 1–100 中的偶數
2. 使用 `continue` 忽略 List 中的特定值並印出剩下的項目
3. 使用 `while` 印出 1–100 中的奇數

```python
exclude = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for i in range(1, 100):
    if i % 2 == 0:
        if i in exclude:
            continue
        else:
            print(i)

j = 1
while j <= 100:
    if j % 2 == 1:
        print(j)
    j += 1
```
