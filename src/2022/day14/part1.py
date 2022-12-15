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
        self.lowest_solid = 0
        self.countRestingSands = 0
        self.solid_points_list = set([])
        self.sand_falls_into_void = False

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


    def findAndSetLowestSolid(self):
        self.lowest_solid = max([point[1] for point in self.solid_points_list])

    def checkCanFall(self, point):
        if not (point[0],point[1]+1) in self.solid_points_list:
            return True, (point[0],point[1]+1)
        elif not (point[0]-1,point[1]+1) in self.solid_points_list:
            return True, (point[0]-1,point[1]+1)
        elif not (point[0]+1,point[1]+1) in self.solid_points_list:
            return True, (point[0]+1,point[1]+1)
        else:
            return False, point

    def reachedVoid(self, point):
        return point[1]-1 == self.lowest_solid

    def dropSand(self):
        #print("Sand dropped")
        canFall, nextPoint = self.checkCanFall((500,0))
        while canFall:
            canFall, nextPoint = self.checkCanFall(nextPoint)
            #print(nextPoint)
            if canFall:
                if self.reachedVoid(nextPoint):
                    self.sand_falls_into_void = True
                    break
            else:
                #print("Sand came to rest at ", nextPoint)
                self.solid_points_list.add(nextPoint)
                self.countRestingSands += 1


if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    start = time.time_ns()
    sum = 0
    caveWorld = World()
    countLines = 0
    for line in req.text.splitlines():
        countLines += 1
        caveWorld.addSolidPointsToList(line)

    caveWorld.findAndSetLowestSolid()
    
    while not caveWorld.sand_falls_into_void:
        caveWorld.dropSand()

    print(caveWorld.countRestingSands)
    end = time.time_ns()
    print(f'Time needed: {(end-start) / 10**6} ms')
else:
    print("Bad request or else")
