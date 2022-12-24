import os
import time
import requests
from dotenv import load_dotenv
load_dotenv()

from enum import Enum



cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/8/input", cookies=cookies)


def check_horizontal(line, check_tree):
    visible = True
    for tree in line:
        if int(tree) >= check_tree:
            visible = False
            break
    return visible


def check_vertical(inputlines, index_tree, check_tree):
    visible = True
    for line in inputlines:
        if int(line[index_tree]) >= check_tree:
            visible = False
            break
    return visible



if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    start = time.time_ns()
    inputlines = req.text.splitlines()
    sum = 0
    for index_line, line in enumerate(inputlines):

        for index_tree, tree in enumerate(line):
            visible = check_horizontal(line[0:index_tree], int(tree))
            if not visible:
                visible = check_horizontal(line[index_tree+1:], int(tree))
                if not visible:
                    visible = check_vertical(inputlines[0:index_line], index_tree, int(tree))
                    if not visible:
                        visible = check_vertical(inputlines[index_line+1:], index_tree, int(tree))
            if visible:
                sum += 1


    print(sum)

    end = time.time_ns()
    print(f'Time needed: {(end-start) / 10**6} ms')
else:
    print("Bad request or else")
