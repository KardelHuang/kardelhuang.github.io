---
title: Day 8 - 條件判斷進階篇
parent: Python
nav_order: 8
---

# 條件判斷進階篇

## 巢狀判斷式結構

藉由縮排，可以讓判斷式產生巢狀結構

```python
score = 95

if score >= 60:
    if score >= 90:
        print("優秀！")
    else:
        print("及格！")
else:
    print("不及格")
```

## 三元運算子

判斷式可以透過三元運算子在單行中完成，結構為 `x if condition else y`

```python
status = "及格" if score >= 60 else "不及格"
print(status)
```

## 練習

1. 根據分數輸出不同評語，並用巢狀 if 判斷等級：
- ≥ 90：A級
- 80~89：B級
- 70~79：C級
- <70：不及格

2. 輸入一個整數，判斷是否：
- 為偶數
- 且大於 50
- 並用三元運算子表示結果為 "合格" 或 "不合格"

```python
score = 100
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "不及格"

print(grade)

i = 51
result = "合格" if i % 2 == 0 and i > 50 else "不合格"

print(result)
```
