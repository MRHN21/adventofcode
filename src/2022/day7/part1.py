import os
import time
import requests
from dotenv import load_dotenv
load_dotenv()

from enum import Enum



cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/7/input", cookies=cookies)


class FileTreeElem():

    def __init__(self, is_file: bool, name: str, parent, size: int = 0) -> None:
        self.childs = []
        self.parent = parent

        self.is_file = is_file
        self.name = name
        self.size = size
        self.sum_size = None


    def get_name(self) -> str:
        return self.name

    def add_childs(self, childs: list):
        for child in childs:
            self.childs.append(child)

    def add_child(self, child):
        self.childs.append(child)

    def get_childs_names(self) -> list[str]:
        return [child.get_name() for child in self.childs]

    def get_child_with_name(self, name):
        for child in self.childs:
            if child.get_name() == name:
                return child
        return None

    def calc_sums(self) -> int:
        sum = 0
        for child in self.childs:
            sum += child.calc_sums()
        sum += self.size
        self.sum_size = sum
        return sum

    def get_parent(self):
        return self.parent

    def is_child(self, name):
        return name in self.get_childs_names()

    def print_tree(self, level: str = ""):
        print(f'{level}_{self.name} sum: {self.sum_size if self.sum_size != None else "-"}   self-size: {self.size if self.size > 0 else ""}')
        level += "  |"
        #print(self.name, self.childs)
        for child in self.childs:
            child.print_tree(level=level)
    
    def get_sum_size_dirs_max_x(self, x: int):
        if self.is_file:
            return 0
        elif self.sum_size <= x:
            return self.sum_size + sum(child.get_sum_size_dirs_max_x(x) for child in self.childs)
        else:
            return sum(child.get_sum_size_dirs_max_x(x) for child in self.childs)
        

if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    start = time.time_ns()
    root = FileTreeElem(is_file=False, name="/", parent=None)
    current_dir = root
    for line in req.text.splitlines():
        if line[0] == "$":
            if line [2:4] == "cd":
                if line[5:] == "..":
                    #print("Going up from",current_dir.get_name() , "to",current_dir.get_parent().get_name() )
                    current_dir = current_dir.get_parent()
                elif line[5:] == "/":
                    current_dir = root
                else:
                    if line[5:] in current_dir.get_childs_names():
                        #print("Going down from", current_dir.get_name() ,"to",current_dir.get_child_with_name(line[5:]).get_name())
                        current_dir = current_dir.get_child_with_name(line[5:])
            elif line[2:4] == "ls":
                continue
        elif line[0:3] == "dir":
            if line[4:] not in current_dir.get_childs_names():
                new_child = FileTreeElem(is_file=False, name=line[4:], parent=current_dir)
                current_dir.add_child(new_child)
        else:
            size_and_name = line.split(" ")
            size = int(size_and_name[0])
            name = size_and_name[1]
            if name not in current_dir.get_childs_names():
                new_child = FileTreeElem(is_file=True, name=name, parent=current_dir, size=size)
                current_dir.add_child(new_child)
    
    root.calc_sums()
    #root.print_tree()

    print(root.get_sum_size_dirs_max_x(100000))




    
    end = time.time_ns()
    print(f'Time needed: {(end-start) / 10**6} ms')
else:
    print("Bad request or else")
