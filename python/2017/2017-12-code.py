import re
from functools import lru_cache
data = open("inputs/2017-12.txt").read().splitlines()

parse = lambda line: [int(x) for x in re.findall("[0-9]+", line)]
source = [parse(line) for line in data]
children = {line[0]:line[1:] for line in source}

def group_size(root, group):
    if root in group:
        return 0

    group.add(root)
    return sum(group_size(child, group) for child in children[root]) + 1

print(group_size(0, set()))
# TODO: continue
