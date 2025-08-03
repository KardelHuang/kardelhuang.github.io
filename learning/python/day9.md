---
title: Day 9 - 函式與參數進階篇
parent: Python
nav_order: 9
---

# 函式與參數進階篇

## 預設參數

函式可以定義預設參數，當沒有傳參數時，會使用預設參數

```python
def greet(name="Kardel"):
    print(f"Hello, {name}!")

greet()            # ➜ Hello, Kardel!
greet("老師")      # ➜ Hello, 老師!
```

## 命名參數

傳參數時，可以指定參數名稱，指定後可以無視函式的參數順序

```python
def show_info(name, age):
    print(f"{name} 是 {age} 歲")

show_info(age=25, name="Kardel")  # 順序不重要
```

## 可變參數

可以在參數加上 `*` 或 `**` ，讓參數變成可接受多參數的形式

```python
def total(*scores):
    return sum(scores)

def show_all(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print(total(80, 90, 85))                 # ➜ 255
show_all(name="Kardel", lang="Python")   # ➜ name: Kardel ...
```

## 變數作用域

變數有分成全域或是區域

```python
x = "全域"

def test():
    x = "區域"
    print(x)

test()      # 區域
print(x)    # 全域
```

## 練習

1. 寫一個 introduce(name, lang="Python") 函式，印出「我是 XX，我正在學習 XX」
2. 建立一個 sum_and_avg(*nums) 函式，回傳總和與平均（用 tuple）
3. 設計 describe_user(**info)，印出使用者所有資訊

```python
def introduce(name, lang="Python"):
    print(f"我是 {name} ，我正在學習 {lang}")

def sum_and_avg(*nums):
    total = sum(nums)
    avg = total / len(nums)
    return total, avg

def describe_user(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

introduce("Amy")
introduce(lang="Python", name="Kardel")

print(sum_and_avg(10, 20, 30))

describe_user(name="Kardel", lang="Python", teacher="Copilot")
```
