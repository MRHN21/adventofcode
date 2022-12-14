import os
import requests
from dotenv import load_dotenv
load_dotenv()

import string

cookies = {"cookie": os.environ.get("COOKIE2022")}
req = requests.get(
    "https://adventofcode.com/2022/day/3/input", cookies=cookies)


dict_lowercase = dict( zip ( string.ascii_lowercase, [x+1 for x in range(26)] ) )
dict_uppercase = dict( zip ( string.ascii_uppercase, [x+27 for x in range(26)] ) )

dict_objects = dict_lowercase | dict_uppercase

if req.status_code == 200 and req.headers['content-type'] == "text/plain":
    print("Start")
    sum = 0
    elveNum = 1
    searchAndAdd = False
    for line in req.text.splitlines():
        if elveNum == 1:
            elveRuckSack1 = line
            elveNum = 2
        elif elveNum == 2:
            elveRuckSack2 = line
            elveNum = 3
        elif elveNum == 3:
            elveRuckSack3 = line
            elveNum = 1
            searchAndAdd = True
        if searchAndAdd:
            length1 = len(elveRuckSack1)
            for object in elveRuckSack1[0:length1]:
                if elveRuckSack2.find(object) != -1 and elveRuckSack3.find(object) != -1:
                    sum += dict_objects[object]
                    searchAndAdd = False
                    break

    print(f'sum {sum}')
else:
    print("Bad request or else")
