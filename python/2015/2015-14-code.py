from collections import defaultdict
import re
data = open("inputs/2015-14.txt").read().splitlines()

def parse(line):
    return [int(values) for values in re.findall("[0-9]+", line)]
source = [parse(line) for line in data]
names = [line.split()[0] for line in data]

def distance_travelled(speed, energy, rest, timeout):
    div, mod = divmod(timeout, energy + rest)
    travel_time = energy * div + min(mod, energy)
    return speed * travel_time

max_distance = max(distance_travelled(*values, 2503) for values in source)
print(max_distance)
# TODO: continue

points = defaultdict(int)
distances = defaultdict(int)
for i in range(2503):
    for name, values in zip(names, source):
        distances[name] = distance_travelled(*values, i+1)

    winner = max(distances.values())
    for name in names:
        points[name] += winner == distances[name]

print(points)
