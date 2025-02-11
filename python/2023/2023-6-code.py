import re
from math import prod
data = open("inputs/2023-6.txt").read().splitlines()

# TODO: complete
source = [[int(x) for x in re.findall(r"\d+", line)] for line in data]
source = [tuple(pair) for pair in zip(*source)]

total_part1 = prod(count_wins
    for time, distance in source
    for count_wins in [sum(1
        for hold in range(time)
        if hold * (time - hold) > distance)
    ]
)
print(total_part1)
