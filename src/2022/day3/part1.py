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
    for line in req.text.splitlines():
        length = len(line)
        halflength = int(length / 2)
        #print(f'length: {length}, halflength: {halflength}')
        #print(f'{line} - {line[0:halflength]} {line[halflength:length]}')
        for object in line[0:halflength]:
            if (line[halflength:length].find(object) != -1):
                sum += dict_objects[object]
                break

    print(f'sum {sum}')
else:
    print("Bad request or else")
