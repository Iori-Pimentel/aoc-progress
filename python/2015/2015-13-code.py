from itertools import permutations
from collections import defaultdict
data = open("inputs/2015-13.txt").read().splitlines()

people = set()
relations = defaultdict(int)
for line in data:
    line = line.strip(".")
    a, _, gl, x, *_, b = line.split()
    x = int(x)
    people |= {a, b}
    relations[(a,b)] += {"gain":x, "lose":-x}[gl]
    relations[(b,a)] += {"gain":x, "lose":-x}[gl]

max_happiness = lambda people: max(
    sum(relations[pair] for pair in zip(circle, circle[1:] + (circle[0],)))
        for circle in permutations(people)
)
print(max_happiness(people), max_happiness(people | {"me"}))
