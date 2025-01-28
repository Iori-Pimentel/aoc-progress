from itertools import batched
import re
data = open("inputs/2015-16.txt").read().splitlines()

def parse(line):
    return (
        re.search("[0-9]+", line).group(),
        [
            (property, int(value))
            for property, value in re.findall(r"([a-z]+): ([0-9]+)", line)
        ]
    )

source = [parse(line) for line in data]
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

def find(func):
    return next(id
        for id, properties in source
        if all(func(*property) for property in properties)
    )

find_part1 = find(lambda key, value: ticker[key] == value)
find_part2 = find(
    lambda key, value:
        ticker[key] < value if key in ["cats", "trees"] else
        ticker[key] > value if key in ["pomeranians", "goldfish"] else
        ticker[key] == value
)
print(find_part1, find_part2)
