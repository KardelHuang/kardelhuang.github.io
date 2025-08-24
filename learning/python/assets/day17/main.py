import argparse
from tools import get_user_info, calc_avg

parser = argparse.ArgumentParser(description="GitHub CLI 工具")
parser.add_argument("username", help="GitHub 使用者名稱")
args = parser.parse_args()

info = get_user_info(args.username)
print(info)
avg_score = calc_avg([80, 90, 100])
print(avg_score)