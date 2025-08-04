def get_score(x):
    try:
        score = int(x)
        if score < 0 or score > 100:
            raise ValueError("無效分數")
    except ValueError as e:
        print("錯誤:", e)
    finally:
        print("流程結束")

get_score(input("分數:"))