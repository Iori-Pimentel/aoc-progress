from itertools import accumulate
data = open("inputs/2015-1.txt").readline()

travel = lambda acc, c: acc + { "(": 1, ")": -1 }[c]
visited = list(accumulate(data, travel, initial=0))

last = visited[-1]
match = next(index for index, floor in enumerate(visited) if floor < 0)
print(last, match)
