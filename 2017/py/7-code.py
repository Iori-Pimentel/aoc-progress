import os
import pprint
import re
from collections import Counter

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()


# dict:
# key = program
# value = weight, children
children = [child for child, _ in re.findall("([a-z]+)(,|$)", input)]
parents = [parent for parent in re.findall(r'([a-z]+)[^\n]+ ->', input)]

root = [parent for parent in parents if not parent in children]

counter = Counter(re.findall(r'[a-z]+', input)).items()
root = [program for program, count in counter if count == 1][0]
print(root)
