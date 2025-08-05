---
title: Day 11 - 檔案讀寫與資料儲存
parent: Python
nav_order: 11
---

# 檔案讀寫與資料儲存

透過 `open` 開啟檔案，可以依據不同模式來開啟，以下是文字檔常見模式
- w: 以新檔案方式進行寫入
- r: 以唯讀方式開啟
- a: 當檔案存在時，從最尾端開始寫入

開啟檔案後，可以使用 `read`、`write`方式進行操作

## 寫入檔案

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("今天學習了檔案儲存功能\n")
```

## 讀取檔案

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

## CSV資料儲存

```python
import csv

data = [["name", "score"], ["Kardel", 95]]
with open("score.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

## 練習

1. 建立成績資料表 score.csv，包含你自定義的幾筆資料
2. 從 score.csv 讀取資料，找出最高分、平均分

```python
import csv

with open("score.csv", "r", newline="", encoding="utf-8") as f:
    rows = csv.DictReader(f)
    highScore = ("", 0)
    scores = []
    
    for row in rows:
        score = int(row["score"])
        if (score > highScore[1]):
            highScore = (row["name"], score)
        scores.append(score)

print(f"最高分 {highScore[0]}: {highScore[1]}")
print(f"平均分: {sum(scores)/len(scores)}")
```