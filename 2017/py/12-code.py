import os
import pprint
import re

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

cache = set()
def count(id, cache):
    if id in cache:
        return 0

    cache.add(id)
    ids = re.search(f"{id} <-> (.*)", input).group(1).split(", ")

    return sum(count(id, cache) for id in ids) + 1

print(count("0", cache))
