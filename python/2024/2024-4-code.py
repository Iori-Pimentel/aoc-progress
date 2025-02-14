from itertools import product
grid = open("inputs/2024-4.txt").read().splitlines()
directions = [direction
    for direction in product([-1, 0, 1], [-1, 0, 1])
    if direction != (0, 0)
]
diagonals = [direction
    for direction in product([-1, 1], [-1, 1])
    if direction != (0, 0)
]

def check_direction(row, col, direction):
    xmas = "XMAS"
    if grid[row][col] != xmas[0]:
        return False

    row_n, col_n = row, col
    row_d, col_d = direction
    for char in xmas[1:]:
        row_n, col_n = row_n + row_d, col_n + col_d
        if not in_bounds(row_n, col_n):
            return False
        if grid[row_n][col_n] != char:
            return False

    return True

def check_x(row, col):
    if grid[row][col] != "A":
        return False

    count = 0
    for diagonal in diagonals:
        row_d, col_d = diagonal
        row_nd, col_nd = row_d * -1, col_d * -1
        row_n, col_n = row + row_d, col + col_d
        row_nn, col_nn = row + row_nd, col + col_nd

        if not in_bounds(row_n, col_n) or not in_bounds(row_nn, col_nn):
            return False

        if grid[row_n][col_n] == "M" and grid[row_nn][col_nn] == "S":
            count += 1

    return count == 2

def in_bounds(row, col):
    return 0 <= row < N and 0 <= col < C

N = len(grid)
C = len(grid[0])
total_part1 = 0
total_part2 = 0
for row in range(N):
    for col in range(C):
        for direction in directions:
            total_part1 += check_direction(row, col, direction)
        total_part2 += check_x(row, col)

print(total_part1, total_part2)
