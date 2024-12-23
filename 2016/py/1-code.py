import os

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

instructions = input.split(", ")
orientation = 0
cx, cy = 0, 0
first_vist_twice = None
visited = set()

for instruction in instructions:
    direction, count = instruction[0], int(instruction[1:])
    orientation = orientation + { "R":1, "L":-1 }[direction]
    orientation = orientation % 4
    dx, dy = {
        0:(0, 1),
        1:(1, 0),
        2:(0, -1),
        3:(-1, 0)
    }[orientation]

    for _ in range(count):
        cx, cy = cx + dx, cy + dy

        if not first_vist_twice and (cx, cy) in visited:
            first_vist_twice = (cx, cy)

        visited.add((cx, cy))

distance = abs(cx) + abs(cy)
print(distance)
print(sum(abs(distance) for distance in first_vist_twice))
