from itertools import permutations, count
data = open("inputs/2024-8.txt").read().splitlines()

antennas = [(row, col,char)
    for row, line in enumerate(data)
    for col, char in enumerate(line)
    if char != "."
]

antinodes = set()
R = len(data)
C = len(data[0])
for (row1, col1, char1), (row2, col2, char2) in permutations(antennas, 2):
    if char1 != char2:
        continue

    antinode_row, antinode_col = 2*row2 - row1, 2*col2 - col1

    if 0 <= antinode_row < R and 0 <= antinode_col < C:
        antinodes.add((antinode_row, antinode_col))

print(len(antinodes))

antinodes = set()
for (row1, col1, char1), (row2, col2, char2) in permutations(antennas, 2):
    if char1 != char2:
        continue

    for i in count():
        antinode_row, antinode_col = row2 + i*(row2 - row1), col2 + i*(col2 - col1)
        if 0 <= antinode_row < R and 0 <= antinode_col < C:
            antinodes.add((antinode_row, antinode_col))
        else:
            break

print(len(antinodes))
