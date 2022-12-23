import os
import time
import requests
from dotenv import load_dotenv
load_dotenv()

from enum import Enum



cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/5/input", cookies=cookies)

class CargoLoadProcessor():

    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.shiplines = []
        self.processlines = []

        self.crates = []

        # parse shiplines and number of crates
        for line in self.lines:
            if "[" in line:
                self.shiplines.append(line)
            else:
                self.num_crates = len(line.split("   "))
                break

        # parse process (move) lines
        for line in self.lines:
            if "move" in line:
                self.processlines.append(line)

        # init cratestacks
        for i in range(self.num_crates):
            self.crates.append([])

        
        # reverse shiplines for easier parsing (when building stacks)
        #print(self.shiplines)
        self.shiplines.reverse()
        #print(self.shiplines)

        #fill crates
        for line_index, line in enumerate(self.shiplines):
            for i in range(self.num_crates):
                index_item = 1 + i  * 4
                #print(f'{i},{index_item},{self.shiplines[line_index][index_item]}:')
                if self.shiplines[line_index][index_item] != " ":
                    self.crates[i].append(self.shiplines[line_index][index_item])


        # move crates
        for line in self.processlines:
            line_parts = line.split(" ")
            move_crates = int(line_parts[1])
            move_from = int(line_parts[3])
            move_to = int(line_parts[5])
            # print(line)
            # print(f'move {move_crates} from {move_from} to {move_to}')
            # print()
            for move in range(move_crates):
                self.crates[move_to-1].append(self.crates[move_from-1].pop())
        
        output = ""
        for crate in self.crates:
            output += crate.pop()
        print(output)


if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    start = time.time_ns()
    CargoLoadProcessor(req.text.splitlines())

    end = time.time_ns()
    print(f'Time needed: {(end-start) / 10**6} ms')
else:
    print("Bad request or else")
