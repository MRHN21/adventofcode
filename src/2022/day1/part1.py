import os
import requests
from dotenv import load_dotenv
load_dotenv()

cookies = {"cookie": os.environ.get("COOKIE2022") }
req = requests.get("https://adventofcode.com/2022/day/1/input", cookies=cookies)


if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    sum = 0
    currentMax = 0
    elve = 1
    elves = []
    for line in req.text.splitlines():
        if line == "":
            elves.append({"elve": elve, "sum": sum})
            if sum > currentMax:
                currentMax = sum
                elveMax = elve
            sum = 0
            elve += 1
        else:
            sum += int(line)
    print(f'Max: {currentMax}, Elve: {elveMax}')
    print(elves)
else:
    print("Bad request or else")