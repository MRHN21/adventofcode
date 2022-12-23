import os
import time
import requests
from dotenv import load_dotenv
load_dotenv()

from enum import Enum



cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/4/input", cookies=cookies)


if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    start = time.time_ns()
    countOverlaps = 0
    for line in req.text.splitlines():
        assignments = line.split(",")
        assign1 = assignments[0].split("-")
        assign2 = assignments[1].split("-")
        assign1_begin = int(assign1[0])
        assign1_end = int(assign1[1])
        assign2_begin = int(assign2[0])
        assign2_end = int(assign2[1])
        cond1_1 = assign1_begin >= assign2_begin and assign1_begin <= assign2_end 
        cond1_2 = assign1_end <= assign2_end and assign1_end >= assign2_begin
        cond2_1 = assign2_begin >= assign1_begin and assign2_begin <= assign1_end 
        cond2_2 = assign2_end <= assign1_end and assign2_end >= assign1_begin
        cond1 = cond1_1 or cond1_2
        cond2 = cond2_1 or cond2_2
        if cond1 or cond2:
            countOverlaps += 1



    print(countOverlaps)
    end = time.time_ns()
    print(f'Time needed: {(end-start) / 10**6} ms')
else:
    print("Bad request or else")
