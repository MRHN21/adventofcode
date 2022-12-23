import os
import time
import requests
from dotenv import load_dotenv
load_dotenv()

from enum import Enum



cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/6/input", cookies=cookies)


if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    start = time.time_ns()
    index = 3
    found = False
    while not found:
        index += 1
        code_to_check = req.text[index-4:index]
        #print(code_to_check)
        found = True
        for letter in code_to_check:
            if code_to_check.count(letter) > 1:
                found = False
                break
    
    print(index)
    end = time.time_ns()
    print(f'Time needed: {(end-start) / 10**6} ms')
else:
    print("Bad request or else")
