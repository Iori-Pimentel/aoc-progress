import os
import pprint

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

mult = 2
cx, cy = 0, 0
spiral = {}
directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]
index = 0
for _ in range(int(input)):
    spiral.add((cx, cy))
    wx, wy = cx + dx, cy + dy
    if (wx, wy) in spiral:
        cx, cy = wx, wy
        index = (index + 1) % len(directions)
    

print(input)
