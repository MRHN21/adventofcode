import os
import requests
from dotenv import load_dotenv
load_dotenv()

cookies = {"cookie": os.environ.get("COOKIE2022") }
req = requests.get("https://adventofcode.com/2022/day/1/input", cookies=cookies)

def takeSum(elem):
    return elem["sum"]

if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    sum = 0
    elve = 1
    elves = []
    for line in req.text.splitlines():
        if line == "":
            elves.append({"elve": elve, "sum": sum})
            sum = 0
            elve += 1
        else:
            sum += int(line)
    elves.sort(key=takeSum, reverse=True)
    print(elves)
    sum_top_three = elves[0]["sum"] + elves[1]["sum"] + elves[2]["sum"]
    print(f'Sum top three: {sum_top_three}')
else:
    print("Bad request or else")