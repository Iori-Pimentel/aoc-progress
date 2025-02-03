import re
from collections import Counter
from math import prod
from functools import reduce
# 12 red cubes, 13 green cubes, and 14 blue
split = [
    (int(id_number), [
        Counter({name: int(count) for count, name in re.findall(r"(\d+) (\w+)", a_section)})
        for a_section in re.split(";", sections)
    ])
    for line in open("inputs/2023-2.txt")
    for id_number, sections in [re.search(r"(\d+): (.*)", line).groups()]
]

available = Counter({"red": 12, "green": 13, "blue": 14})

valid_total = sum(id_number
    for id_number, sections in split
    if all(available >= a_section for a_section in sections)
)

union = lambda counters: reduce(lambda acc, c: acc | c, counters)
power_total = sum(prod(union(sections).values())
    for id_number, sections in split
)
print(valid_total, power_total)
