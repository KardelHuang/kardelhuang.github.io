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
