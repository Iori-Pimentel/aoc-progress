from math import prod
data = open("inputs/2020-3.txt").read().splitlines()

def collisions(dx, dy):
    x, y = 0, 0
    total = 0
    while y != len(data)-1:
        x += dx
        x %= len(data[1])
        y += dy
        if data[y][x] == "#":
            total += 1
    return total

print(collisions(3, 1))
print(prod(collisions(x, y) for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))

