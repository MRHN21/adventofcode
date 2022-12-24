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
    sc_sc = 0
    for tree in line:
        sc_sc += 1
        if int(tree) >= check_tree:
            break
    return sc_sc


def check_vertical(inputlines, index_tree, check_tree):
    sc_sc = 0
    if inputlines is not None:
        for line in inputlines:
            sc_sc += 1
            if int(line[index_tree]) >= check_tree:
                break
    else:
        return 1
    return sc_sc



if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    start = time.time_ns()
    inputlines = req.text.splitlines()
    max_scenic_score = 0
    for index_line, line in enumerate(inputlines):

        for index_tree, tree in enumerate(line):
            sc_sc_l = check_horizontal(line[0:index_tree][::-1], int(tree))
            sc_sc_r = check_horizontal(line[index_tree+1:], int(tree))
            inputlines_loc = inputlines[0:index_line]
            inputlines_loc.reverse()
            sc_sc_u = check_vertical(inputlines_loc, index_tree, int(tree))
            sc_sc_d = check_vertical(inputlines[index_line+1:], index_tree, int(tree))

            loc_sc_sc = sc_sc_l * sc_sc_r * sc_sc_u * sc_sc_d
            max_scenic_score = loc_sc_sc if loc_sc_sc > max_scenic_score else max_scenic_score

    print(max_scenic_score)

    end = time.time_ns()
    print(f'Time needed: {(end-start) / 10**6} ms')
else:
    print("Bad request or else")
