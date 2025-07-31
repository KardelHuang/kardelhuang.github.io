---
title: Day 6 - 條件判斷與邏輯運算
parent: Python
nav_order: 6
---

# 條件判斷與邏輯運算

- 條件語法: `if`, `elif`, `else`
- 布林運算子: `and`, `or`, `not`
- 比較運算子: `==`, `!=`, `<`, `<=`, `>`, `>=`

## 條件語法

```python
temperature = 30

if temperature > 32:
    print("今天太熱啦！")
elif temperature < 20:
    print("有點冷，穿件外套吧～")
else:
    print("天氣剛剛好 ☀️")

if score > 60 and score < 90:
    print("普通表現")
```

- Python 不使用 `{}`，而是用縮牌表示區塊
- 可以用布林運算子`and`, `or`, `not`來做多重條件

## 練習

1. 輸入一個分數，輸出等級（例如：A、B、C）

```python
score = 90
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print("你的成績是", grade)
```
