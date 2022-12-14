import os
import requests
from dotenv import load_dotenv
load_dotenv()

cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/2/input", cookies=cookies)

#A = Rock
#B = Paper
#C = Scissors

#X = Loose
#Y = Draw
#Z = Win
game_result_dict = {
    "A X": 3,  # X = Lose = 0,  Scissors = 3,   T = 3
    "A Y": 4,  # Y = Draw = 3,  Rock = 1,       T = 4
    "A Z": 8,  # Z = Win = 6,   Paper = 2,      T = 8
    "B X": 1,  # X = Lose = 0,  Rock = 1,       T = 1
    "B Y": 5,  # Y = Draw = 3,  Paper = 2,      T = 5
    "B Z": 9,  # Z = Win = 6,   Scissors = 3,   T = 9
    "C X": 2,  # X = Lose = 0,  Paper = 2,      T = 2
    "C Y": 6,  # Y = Draw = 3,  Scissors = 3,   T = 6
    "C Z": 7   # Z = Win = 6,   Rock = 1,       T = 7
}


if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    count_games = {
        "A X": 0,
        "A Y": 0,
        "A Z": 0,
        "B X": 0,
        "B Y": 0,
        "B Z": 0,
        "C X": 0,
        "C Y": 0,
        "C Z": 0
    }
    for line in req.text.splitlines():
        count_games[line] += 1

    total = sum([game_result_dict[elem] *
                           count_games[elem] for elem in game_result_dict])

    print(f'total {total}')
else:
    print("Bad request or else")
