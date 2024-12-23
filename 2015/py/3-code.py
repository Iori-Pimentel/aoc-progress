import os

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()


def add_houses(input):
    cx, cy = 0, 0
    houses.add((cx, cy))
    for char in input:
        dx, dy = {
            "^":(0, 1),
            "<":(-1, 0),
            ">":(1, 0),
            "v":(0, -1)
        }[char]
        cx, cy = cx + dx, cy + dy
        houses.add((cx, cy))

houses = set()
add_houses(input)
print(len(houses))

houses = set()
add_houses(input[::2])
add_houses(input[1::2])
print(len(houses))
