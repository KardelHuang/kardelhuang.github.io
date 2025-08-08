---
title: Day 14 - 函式進階技巧
parent: Python
nav_order: 14
---

# 函式進階技巧

## 可變參數

- 一維可變參數 `*args`
- 二維可變參數 `**kwargs`

```python
def show_scores(*scores):
    print("總分：", sum(scores))

def show_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
```

## 匿名函式

- 可使用 `lambda` 宣告匿名函式

```python
add = lambda x, y: x + y
print(add(3, 5))  # ➜ 8
```

## 搭配高階函式

```python
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))       # ➜ [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, nums))  # ➜ [2, 4]
```

## 練習

1. 使用 lambda 搭配 map() 計算一組數字的立方
2. 建立一個 sort_by_length(words) 函式，使用 sorted() 搭配 lambda 依字串長度排序

```python
nums = list(range(1, 5))
cube = list(map(lambda x: x**3, nums))
print(cube)

def sort_by_length(words):
    return sorted(words, key=lambda x: len(x))

words = ["alpha", "beta", "charlie", "delta", "echo"]
print(sort_by_length(words))
```
