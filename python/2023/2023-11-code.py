# set of doubled row and cols
# then union to find count of double
from itertools import combinations
data = open("inputs/2023-11.txt").read().splitlines()
rotated = ["".join(column) for column in zip(*data)]
doubled_rows = {row for row, line in enumerate(data) if "#" not in line}
doubled_cols = {col for col, line in enumerate(rotated) if "#" not in line}

galaxies = [(row, col)
    for row, line in enumerate(data)
    for col, char in enumerate(line)
    if char == "#"
]

def distance(row_a, col_a, row_b, col_b, offset):
    offset -= 1
    row_a, row_b = sorted([row_a, row_b])
    col_a, col_b = sorted([col_a, col_b])
    rows = range(row_a, row_b)
    cols = range(col_a, col_b)

    row_distance = len(rows) + len(doubled_rows & set(rows)) * offset
    col_distance = len(cols) + len(doubled_cols & set(cols)) * offset
    return row_distance + col_distance

distances_part1 = sum(distance(*a, *b, offset=2) for a, b in combinations(galaxies, 2))
distances_part2 = sum(distance(*a, *b, offset=1000000) for a, b in combinations(galaxies, 2))
print(distances_part1, distances_part2)
