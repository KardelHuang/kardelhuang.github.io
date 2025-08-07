---
title: Day 13 - 資料壓縮與結構強化
parent: Python
nav_order: 13
---

# 資料壓縮與結構強化

## List Comprehension

透過 `[x for x in list if condition]` 可以快速生成清單

```python
squares = [x**2 for x in range(10)]  # ➜ [0, 1, 4, ..., 81]
evens = [x for x in range(20) if x % 2 == 0]
```

## zip

透過 `zip(list1, list2)` 可以合併成 `tuple` 結構

```python
names = ["Kardel", "老師"]
scores = [95, 88]
combined = list(zip(names, scores))  # ➜ [('Kardel', 95), ('老師', 88)]
```

## enumerate

透過 `enumerate(list)` 可以取得索引與內容

```python
for i, name in enumerate(names):
    print(f"{i}: {name}")
```

## 練習

1. 建立一個立方清單
2. 建立一個函式 tag_notes(notes: list)，回傳 [(index, note)] 結構

```
cube = [x**3 for x in range(1, 10)]
print(cube)

def tag_notes(notes: list):
    indexes = []
    titles = []
    for i, t in enumerate(notes):
        indexes.append(i)
        titles.append(t)
    return list(zip(indexes, titles))

print(tag_notes(["檔案讀寫與資料儲存", "資料清理與文字格式化", "資料壓縮與結構強化"]))
```
