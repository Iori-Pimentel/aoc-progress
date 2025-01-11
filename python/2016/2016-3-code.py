from itertools import chain, batched
data = open("inputs/2016-3.txt").read().splitlines()

def is_triangle(sides):
    sides = sorted(sides)
    return sides[0]+sides[1] > sides[2]

horizontal = [[int(x) for x in line.split()] for line in data]
vertical = batched(chain.from_iterable(zip(*horizontal)), 3)

horizontal_count = sum(map(is_triangle, horizontal))
vertical_count = sum(map(is_triangle, vertical))

print(horizontal_count, vertical_count)
