---
title: Day 4 - List & Tuple
parent: Python
nav_order: 4
---

# List & Tuple

在一維資料中，有`list`和`tuple`可以選擇，`list`為可變型別，`tuple`為不可變型別

以下是範例

```python
# List（可變）
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')       # 新增元素
fruits[1] = 'blueberry'       # 修改元素
print(fruits[:2])             # 切片取前兩個
print(sorted(fruits))         # 排序但不改變原 list
fruits.sort()                 # 就地排序

# Tuple（不可變）
scores = (90, 85, 88)
print(scores[0])              # 取值，但不能修改
```

## 練習

1. 建立一個 list temperatures 儲存一週氣溫，並列出最高與最低
2. 建立一個 tuple weekdays 儲存週一到週日
3. 嘗試使用 for 迴圈列出 temperatures，並標示每筆資料的「星期幾」
4. 對 temperatures 排序後列出中位數（提示：用 sorted()）

```python
temperatures = [27.5, 26.9, 28.3, 30.1, 31.2, 30.6, 29.8]
weekdays = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
for i, temp in enumerate(temperatures, 0):
    print(f"{weekdays[i]}: {temp} °C")
print(f"中位數: {sorted(temperatures)[3]}")
```
