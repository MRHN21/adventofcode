import os
import time
import requests
from dotenv import load_dotenv
load_dotenv()

from enum import Enum



cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/9/input", cookies=cookies)


class Direction():

    def __init__(self) -> None:
        pass


class RopePiece():

    def __init__(self) -> None:
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0

    def move_head_one(self, direction):
        #update x,y head
        if direction == "D":
            self.head_y = self.head_y - 1
        elif direction == "U":
            self.head_y = self.head_y + 1
        elif direction == "R":
            self.head_x = self.head_x + 1
        elif direction == "L":
            self.head_x = self.head_x - 1
            

    def move_tail_one(self, direction):
        #update x,y tail
        if direction == "D":
            self.tail_y = self.tail_y - 1
        elif direction == "U":
            self.tail_y = self.tail_y + 1
        elif direction == "R":
            self.tail_x = self.tail_x + 1
        elif direction == "L":
            self.tail_x = self.tail_x - 1

    def determine_tail_move_and_move_tail(self):
        move_tail_x = False
        move_tail_y = False
        if abs(self.head_x - self.tail_x) > 1:
            move_tail_x = True
        if abs(self.head_y - self.tail_y) > 1:
            move_tail_y = True
        
        if move_tail_x or move_tail_y:
            if self.head_x > self.tail_x:
                self.move_tail_one("R")
            elif self.head_x < self.tail_x:
                self.move_tail_one("L")
            if self.head_y > self.tail_y:
                self.move_tail_one("U")
            elif self.head_y < self.tail_y:
                self.move_tail_one("D")




    def one_step(self, direction):
        self.move_head_one(direction)
        #determine case
        self.determine_tail_move_and_move_tail()

    def one_step_set_head(self, head_x, head_y):
        self.head_x = head_x
        self.head_y = head_y
        #determine case
        self.determine_tail_move_and_move_tail()

    def get_tail(self):
        return self.tail_x, self.tail_y
    

class LastRopePiece(RopePiece):

    def __init__(self) -> None:
        super().__init__()
        self.visited = set()
        self.visited.add((0,0))

    def determine_tail_move_and_move_tail(self):
        super().determine_tail_move_and_move_tail()
        self.visited.add((self.tail_x, self.tail_y))

    def get_fields_visited_by_tail(self):
        return self.visited

class Rope():

    def __init__(self, pieces) -> None:
        self.pieces = [RopePiece() for i in range(pieces-1)]
        self.last_rope_piece = LastRopePiece()

    def simulate_move(self, direction, amount):
        for i in range(amount):
            for index, piece in enumerate(self.pieces):
                if index == 0:
                    piece.one_step(direction)
                else:
                    t_x, t_y = self.pieces[index-1].get_tail()
                    piece.one_step_set_head(t_x, t_y)
            self.last_rope_piece.one_step_set_head(t_x, t_y)
    
    def get_last_ropepiece(self):
        return self.last_rope_piece


if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    start = time.time_ns()
    inputlines = req.text.splitlines()
    sum = 0
    rope = Rope(10)
    #inputlines = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
    #inputlines = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]
    for line in inputlines:
        input = line.split(" ")
        direction = input[0]
        amount = int(input[1])
        rope.simulate_move(direction, amount)

    print(len(rope.get_last_ropepiece().get_fields_visited_by_tail()))
    end = time.time_ns()
    print(f'Time needed: {(end-start) / 10**6} ms')
else:
    print("Bad request or else")
