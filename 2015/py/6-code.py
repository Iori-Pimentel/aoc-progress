import os

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

instructions = input.split("\n")

grid_1 = [[0] * 1000 for _ in range(1000)]
grid_2 = [[0] * 1000 for _ in range(1000)]
sum_lights = 0
for instruction in instructions:
    (x1, y1), _, (x2, y2) = [pair.split(",") for pair in instruction.split()[-3:]]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if "turn off" in instruction:
                grid_1[x][y] = False
                grid_2[x][y] = max(0, grid_2[x][y] - 1)
            elif "turn on" in instruction:
                grid_1[x][y] = True
                grid_2[x][y] = grid_2[x][y] + 1
            elif "toggle" in instruction:
                grid_1[x][y] = not grid_1[x][y]
                grid_2[x][y] = grid_2[x][y] + 2
            else:
                raise ValueError("No instruction")

count = sum(sum(row) for row in grid_1)
print(count)
count = sum(sum(row) for row in grid_2)
print(count)
