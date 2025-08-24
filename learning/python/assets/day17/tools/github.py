import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return {
            "login": data["login"],
            "repos": data["public_repos"]
        }
    else:
        return {"error": "找不到使用者"}