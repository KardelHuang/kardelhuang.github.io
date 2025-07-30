---
title: Day 5 - Dictionary & Set
parent: Python
nav_order: 5
---

# Dictionary & Set

`dictionary`是一個key-value結構 `{key: value}`，可以用在配對資料（像是名稱對應電話、帳號對應資訊）

`set`是一個集合結構 `{element1, element2}`，用在集合運算（交集、聯集、差集）

## 練習

1. 建立一個字典，記錄你每天學習主題
2. 輸入兩組資料，找出相同元素

```python
lesson = {
    "day1": "安裝環境",
    "day2": "變數與資料型別",
    "day3": "函式與模組",
    "day4": "List & Tuple",
    "day5": "Dictionary & Set"
}

set1 = {1, 2, 4, 8}
set2 = {2, 3, 5, 7}

print(set1.intersection(set2))
```
