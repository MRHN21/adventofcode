import os
import time
import requests
from dotenv import load_dotenv
load_dotenv()

from enum import Enum


cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/14/input", cookies=cookies)


class World():

    def __init__(self):
        self.floor = 0
        self.count_resting_sands = 0
        self.solid_points_list = set([])
        self.source_blocked = False

    def addSolidPointsToList(self, line: str):
        coords_list = line.split(" -> ")
        while coords_list:
            if len(coords_list) > 1:
                coords1 = coords_list[0].split(",")
                x1 = int(coords1[0])
                y1 = int(coords1[1])
                coords2 = coords_list[1].split(",")
                x2 = int(coords2[0])
                y2 = int(coords2[1])
                if y2 > y1:
                    while y2 >= y1:
                        self.solid_points_list.add( (x1, y2) )
                        y2 -= 1
                elif y1 > y2:
                    while y1 >= y2:
                        self.solid_points_list.add( (x1, y1) )
                        y1 -= 1
                elif x2 > x1:
                    while x2 >= x1:
                        self.solid_points_list.add( (x2, y1) )
                        x2 -= 1
                elif x1 > x2:
                    while x1 >= x2:
                        self.solid_points_list.add( (x1, y1) )
                        x1 -= 1
            del coords_list[0]


    def findAndSetFloor(self):
        self.floor = max([point[1] for point in self.solid_points_list])+2

    def checkCanFall(self, point):
        if not (point[0],point[1]+1) in self.solid_points_list and point[1]+1 != self.floor:
            return True, (point[0],point[1]+1)
        elif not (point[0]-1,point[1]+1) in self.solid_points_list and point[1]+1 != self.floor:
            return True, (point[0]-1,point[1]+1)
        elif not (point[0]+1,point[1]+1) in self.solid_points_list and point[1]+1 != self.floor:
            return True, (point[0]+1,point[1]+1)
        else:
            return False, point

    def reachedFloor(self, point):
        return point[1]-1 == self.floor

    def dropSand(self):
        #print("Sand dropped")
        canFall, next_point = self.checkCanFall((500,0))
        if next_point == (500,0):
            #print("Sand came to rest at ", next_point)
            self.solid_points_list.add(next_point)
            self.count_resting_sands += 1
            self.source_blocked = True
        while canFall:
            canFall, next_point = self.checkCanFall(next_point)
            #print(next_point)
            if not canFall:
                #print("Sand came to rest at ", next_point)
                self.solid_points_list.add(next_point)
                self.count_resting_sands += 1
                # if next_point == (500,0):
                #     self.source_blocked = True


if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    start = time.time_ns()
    sum = 0
    caveWorld = World()
    countLines = 0
    for line in req.text.splitlines():
        countLines += 1
        caveWorld.addSolidPointsToList(line)

    caveWorld.findAndSetFloor()
    
    while not caveWorld.source_blocked:
        caveWorld.dropSand()

    print(caveWorld.count_resting_sands)
    end = time.time_ns()
    print(f'Time needed: {(end-start) / 10**6} ms')
else:
    print("Bad request or else")
