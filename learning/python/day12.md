---
title: Day 12 - 資料清理與文字格式化
parent: Python
nav_order: 12
---

# 資料清理與文字格式化

## 字串處理

- `strip` 去除頭尾空白與換行
- `split` 分割字串
- `replace` 替換字詞

```python
text = "   Hello, Kardel!  \n"
cleaned = text.strip()                      # 去除頭尾空白與換行
words = cleaned.split(",")                 # 拆分為 ['Hello', ' Kardel!']
replaced = cleaned.replace("Kardel", "老師")  # 替換字詞
```

## 文字格式化

- `join` 將list放入特定文字並組成字串
- `format` 將`{}`用後續提供的參數取代

```python
joined = " | ".join(["Day", "12", "Notes"])  # ➜ 'Day | 12 | Notes'
formatted = "你好 {}, 今天是 Day {}".format("Kardel", 12)  # 舊式格式化
fstring = f"你好 {cleaned}, 今天進度 Day {12}"               # f-string 格式化
```

## 練習

1. 清理一段資料列：" Name: Kardel, Score: 100 \n" ➜ 拆成字典物件
2. 建立函式 clean_text(text: str)，自動處理換行、空白與多個空格為單一空格

```python
text = " Name: Kardel, Score: 100 \n"
dict = {}
words = text.strip().split(", ")
for word in words:
    dict.update({word.split(": ")[0]: word.split(": ")[1]})

print(dict)

def clean_text(text: str):
    clean_list = [word.strip() for word in text.split(" ") if word]
    return " ".join(clean_list)

print(clean_text("a bb ccc   dd \ne  \nf  g"))
```
