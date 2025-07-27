---
title: Day 2 - 變數與資料型別
parent: Python
nav_order: 2
---

# 變數與資料型別

Python 是動態型別語言，不需要指定型別
常見資料型別：`int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set`

```python
# 整數
a = 42

# 浮點數
b = 3.14

# 字串
c = "Hello, Kardel!"

# 布林值
d = True

# List（類似 C# 的 List<T>）
e = [1, 2, 3]

# Dictionary（類似 C# 的 Dictionary<TKey, TValue>）
f = {"name": "Kardel", "language": "Python"}

# Tuple（不可變的序列）
g = (10, 20)

# Set（不重複元素集合）
h = {1, 2, 3, 2}
```

## 檢查型別

可以使用`type()`來檢查型別

```python
x = 10
print(type(x))  # <class 'int'>
```

## 型別轉換

可以透過以下方式做轉換

```python
x = "123"
y = int(x)      # 轉成整數
z = float(x)    # 轉成浮點數
s = str(456)    # 轉成字串
```

## 練習

1. 建立一個變數 temp，儲存今天的氣溫（浮點數）
2. 建立一個字典 user，包含你的名字與學習語言
3. 建立一個 list scores，包含三個分數，並計算平均值
4. 使用 type() 印出每個變數的型別

```python
temp = 28.8
user = {"name": "Kardel", "language": "python"}
scores = [88, 79, 97]
print(type(temp))
print(type(user))
print(type(scores))
```

結果如下
```shell
> python day2.py
<class 'float'>
<class 'dict'>
<class 'list'>
```
