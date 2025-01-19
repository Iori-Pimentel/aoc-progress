from itertools import batched
import re
data = open("inputs/2015-16.txt").read().splitlines()

def parse(line):
    line = re.findall(r"\b[a-z0-9]+", line)
    return line

source = [parse(line) for line in data]
source = {name: dict(zip(items[0::2], items[1::2])) for name, *items in source}

ticker = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

max_match = max(sum(ticker[key] == value for key, value in items.items())
    for name, items in source.items()
)
print(max_match)
