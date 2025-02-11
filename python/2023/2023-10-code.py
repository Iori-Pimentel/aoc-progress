from collections import deque
data = open("inputs/2023-10.txt").read().splitlines()

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
directions = {
    "S": [NORTH, SOUTH, EAST, WEST],
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
    ".": [],
}

R = len(data)
C = len(data[0])

neighbours = dict()
for row, line in enumerate(data):
    for col, char in enumerate(line):
        next_to = list()
        for dx, dy in directions[char]:
            n_row, n_col = row + dy, col + dx
            if 0 <= n_row < R and 0 <= n_col < C:
                next_to.append((n_row,n_col))
        neighbours[(row, col)] = next_to

start = [(row, col)
    for row, line in enumerate(data)
    for col, char in enumerate(line)
    if char == "S"
].pop()

queue = deque([start])
seen = set()
distance = [[None] * C for _ in range(R)]

distance[start[0]][start[1]] = 0

max_distance = 0
while queue:
    row, col = queue.popleft()
    seen.add((row, col))
    for n_row, n_col in neighbours[(row, col)]:
        if (n_row, n_col) in seen:
            continue
        if (row, col) in neighbours[(n_row, n_col)]:
            distance[n_row][n_col] = distance[row][col] + 1
            max_distance = max(max_distance, distance[n_row][n_col])
            queue.append((n_row, n_col))

print(max_distance)
