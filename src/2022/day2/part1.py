import os
import requests
from dotenv import load_dotenv
load_dotenv()

cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/2/input", cookies=cookies)

#A = X = Rock
#B = Y = Paper
#C = Z = Scissors

game_result_dict = {
    "A X": 4,  # X = Rock = 1,      Draw = 3,   T = 4
    "A Y": 8,  # Y = Paper = 2,     Win = 6,    T = 8
    "A Z": 3,  # Z = Scissors = 3,  Lose = 0,   T = 3
    "B X": 1,  # X = Rock = 1,      Lose = 0,   T = 1
    "B Y": 5,  # Y = Paper = 2,     Draw = 3,   T = 5
    "B Z": 9,  # Z = Scissors = 3,  Win = 6,    T = 9
    "C X": 7,  # X = Rock = 1,      Win = 6,    T = 7
    "C Y": 2,  # Y = Paper = 2,     Lose = 0,   T = 2
    "C Z": 6   # Z = Scissors = 3,  Draw = 3,   T = 6
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
