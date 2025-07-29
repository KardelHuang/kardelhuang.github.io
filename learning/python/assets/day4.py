temperatures = [27.5, 26.9, 28.3, 30.1, 31.2, 30.6, 29.8]
weekdays = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
for i, temp in enumerate(temperatures, 0):
    print(f"{weekdays[i]}: {temp} °C")
print(f"中位數: {sorted(temperatures)[3]}")