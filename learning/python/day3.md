---
title: Day 3 - 函式與模組
parent: Python
nav_order: 3
---

# 函式與模組

## 函式

Python 使用 `def` 定義函式，函式可以有參數與回傳值，當沒有指定`return`時，預設回傳`None`

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Kardel"))  # Hello, Kardel!
```

## 模組

模組是一個`.py`檔案，可以放函式、變數、類別等。可以把常用的函式寫在模組中，然後在其他程式匯入使用

建立一個 `day3_utils.py`
```python
# day3_utils.py
def square(x):
    return x * x

def cube(x):
    return x ** 3
```

在主程式中匯入使用
```python
import day3_utils

print(day3_utils.square(4))  # 16
print(day3_utils.cube(3))    # 27
```

也可以用`from ... import ...`
```python
from day3_utils import square

print(square(5))  # 25
```

### 練習

1. 定義一個函式 add(a, b)，回傳兩數相加結果
2. 定義一個函式 is_even(n)，判斷是否為偶數
3. 定義一個函式 summary(scores)，回傳平均值與最大值（用 tuple）
4. 匯入 `day3_utils` ，並印出 5 的平方與 3 的立方

```python
def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def summary(scores):
    average = sum(scores) / len(scores)
    maximum = max(scores)
    return (average, maximum)

from day3_utils import square

print(square(5))

import day3_utils

print(day3_utils.cube(3))
```
