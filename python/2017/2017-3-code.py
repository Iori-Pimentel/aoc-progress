from itertools import chain, product
data = open("inputs/2017-3.txt").read()

def spiral_formula(spiral_area):
    square_length = int(spiral_area ** 0.5)
    square_area = square_length ** 2
    square_corner = square_length - 1
    if square_area == spiral_area:
        return square_corner

    bigger_square_corner = square_corner + 2
    bigger_square_midpoint = bigger_square_corner // 2 + 1
    ring_distances = list(chain(
        range(bigger_square_corner - 1, bigger_square_midpoint, -1),
        range(bigger_square_midpoint, bigger_square_corner + 1)  # inclusive-range
    )) * 4

    ring_area = spiral_area - square_area
    return ring_distances[ring_area - 1]  # zero-indexing

print(spiral_formula(int(data)))

neighbours = lambda x, y: sum(grid.get((x + dx, y + dy), 0)
    for dx, dy in product([0, 1, -1], repeat=2)
    if not (dx == 0 and dy == 0)
)

def spiral(square_length):
    yield from ((square_length, up) for up in range(-square_length + 1, square_length))
    yield from ((left, square_length) for left in range(square_length, -square_length, -1))
    yield from ((-square_length, down) for down in range(square_length, -square_length, -1))
    yield from ((right, -square_length) for right in range(-square_length, square_length + 1))
    yield from spiral(square_length + 1)

grid = {(0, 0): 1}
for position in spiral(1):
    grid[position] = neighbours(*position)
    if grid[position] > int(data):
        break

print(grid[position])
