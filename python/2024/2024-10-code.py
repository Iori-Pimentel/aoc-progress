from functools import lru_cache
data = open("inputs/2024-10.txt").read().splitlines()

def trail(position):
    if position in seen:
        return 0

    seen.add(position)

    if grid[position] == 9:
        return 1

    count = 0
    for neighbour in [position + 1j, position - 1j, position + 1, position - 1]:
        if neighbour not in grid:
            continue
        if grid[neighbour] - grid[position] == 1:
            count += trail(neighbour)

    return count

grid = {(row * -1j + col): int(char)
    for row, line in enumerate(data)
    for col, char in enumerate(line)
}

starts = [position
    for position in grid
    if grid[position] == 0
]

total = 0
for start in starts:
    seen = set()
    total += trail(start)
# TODO: part1 and part2
print(total)
