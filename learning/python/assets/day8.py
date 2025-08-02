score = 100
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "不及格"

print(grade)

i = 51
result = "合格" if i % 2 == 0 and i > 50 else "不合格"

print(result)
