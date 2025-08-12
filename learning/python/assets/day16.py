import requests
import pandas as pd
from rich.console import Console

account = input("請輸入 GitHub 帳號: ")
res = requests.get(f"https://api.github.com/users/{account}")
data = res.json()
public_repos = data["public_repos"]
console = Console()
console.print(f"公開 Repo 數: {public_repos}", style="bold cyan")