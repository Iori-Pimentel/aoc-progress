from re import findall
from itertools import product
data = open("inputs/2015-6.txt").read().splitlines()

def numbers(line):
    return map(int, findall("[0-9]+", line))

grid_size = range(1000)
grid_part1 = [[0 for _ in grid_size] for _ in grid_size]
grid_part2 = [[0 for _ in grid_size] for _ in grid_size]
for line in data:
    x1, y1, x2, y2 = numbers(line)
    x2, y2 = x2+1, y2+1  # inclusive range
    xs, ys = range(x1, x2), range(y1, y2)

    for x, y in product(xs, ys):
        if "on" in line:
            grid_part1[x][y] = 1
            grid_part2[x][y] += 1
        elif "off" in line:
            grid_part1[x][y] = 0
            grid_part2[x][y] = max(0, grid_part2[x][y] - 1)
        elif "toggle" in line:
            grid_part1[x][y] = 1 - grid_part1[x][y]
            grid_part2[x][y] += 2

# TODO: convet to dict with functions
sum_part1 = sum(map(sum, grid_part1))
sum_part2 = sum(map(sum, grid_part2))
print(sum_part1, sum_part2)
