from functools import cache
data = open("inputs/2024-6.txt").read().splitlines()

NORTH = 1j
EAST = 1
SOUTH = -1j
WEST = -1
directions = [NORTH, EAST, SOUTH, WEST]

grid = {row * SOUTH + col * EAST: char
    for row, line in enumerate(data)
    for col, char in enumerate(line)
}

start = next(position
    for position in grid
    if grid[position] == "^"
)

def rotate(direction):
    next_rotation = (directions.index(direction) + 1) % len(directions)
    return directions[next_rotation]

def escape(position, direction):
    traversed = set()
    while position in grid:
        if (position, direction) in traversed:
            return None

        traversed.add((position, direction))
        if grid.get(position + direction) == "#":
            direction = rotate(direction)
        else:
            position += direction

    return traversed

traversed = escape(start, NORTH)
unique_traversed = set(position for position, _ in traversed)
print(len(unique_traversed))

infinite_loops = 0
unique_traversed.discard(start)
for new_blockade in unique_traversed:
    grid[new_blockade] = "#"
    if escape(start, NORTH) is None:
        infinite_loops += 1
    grid[new_blockade] = "."

print(infinite_loops)
