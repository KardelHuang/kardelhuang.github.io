exclude = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for i in range(1, 100):
    if i % 2 == 0:
        if i in exclude:
            continue
        else:
            print(i)

j = 1
while j <= 100:
    if j % 2 == 1:
        print(j)
    j += 1
