import os
import pprint
import re

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

grid = [[0] * 50 for _ in range(70)]

def shift(amount, row, grid):
    amount = amount % len(grid[row])
    return grid[row][-amount:] + grid[row][:-amount]

def rotate(grid):
    return [list(column) for column in zip(*grid)]

def power(x, y, grid):
    for x in range(x):
        for y in range(y):
            grid[y][x] = 1

lines = input.split("\n")
for line in lines:
    match = re.search(r'rect ([0-9]+)x([0-9]+)', line)
    if match:
        a, b = match.groups()
        power(int(a), int(b), grid)
        continue

    orientation, position, amount = re.search(r'(.)=([0-9]+) by ([0-9]+)$', line).groups()

    if orientation == "x":
        grid = rotate(grid)
    grid[int(position)] = shift(int(amount), int(position), grid)
    if orientation == "x":
        grid = rotate(grid)

print(sum(sum(row) for row in grid))
