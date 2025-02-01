import re
from itertools import product
from collections import defaultdict
data = open("inputs/2018-3.txt").read().splitlines()

source = [[int(x) for x in re.findall("[0-9]+", line)] for line in data]
counter = defaultdict(int)
for val in source:
    id, x, y, w, h = val
    for xa, ya in product(range(x, x+w), range(y, y+h)):
        counter[(xa, ya)] += 1

print(sum(1 for count in counter.values() if count > 1))
for val in source:
    id, x, y, w, h = val

    invalid = False
    for xa, ya in product(range(x, x+w), range(y, y+h)):
        if counter[(xa, ya)] > 1:
            invalid = True
            break
    if not invalid:
        print(id)
        break
