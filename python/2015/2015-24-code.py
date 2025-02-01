from itertools import combinations
from math import prod
data = open("inputs/2015-24.txt").read().splitlines()

weights = [int(x) for x in data]
min_part1 = min(
    (len(a), prod(a))
    for a, b, c in [[[1], [1], [1]]]
    if sum(a) == sum(b) == sum(c)
    if sorted([len(a), len(b), len(c)])[0] == len(a)
)

print(min_part1)
