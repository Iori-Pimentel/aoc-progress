from itertools import permutations
data = open("inputs/2015-9.txt").read().splitlines()

locations = set()
relations = dict()
for line in data:
    a, _, b, _, x = line.split()

    locations |= {a, b}
    relations[(a, b)] = x
    relations[(b, a)] = x

routes = [sum(int(relations[pair]) for pair in zip(route, route[1:]))
    for route in permutations(locations)
]
print(min(routes), max(routes))

