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
