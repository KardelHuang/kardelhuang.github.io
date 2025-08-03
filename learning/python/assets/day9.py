def introduce(name, lang="Python"):
    print(f"我是 {name} ，我正在學習 {lang}")

def sum_and_avg(*nums):
    total = sum(nums)
    avg = total / len(nums)
    return total, avg

def describe_user(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

introduce("Amy")
introduce(lang="Python", name="Kardel")

print(sum_and_avg(10, 20, 30))

describe_user(name="Kardel", lang="Python", teacher="Copilot")
