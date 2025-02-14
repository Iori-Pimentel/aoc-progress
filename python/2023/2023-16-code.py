data = open("inputs/2023-16.txt").read().splitlines()
grid = {(row*-1j + col): char
    for row, line in enumerate(data)
    for col, char in enumerate(line)
}

NORTH = 1j
SOUTH = -1j
EAST = 1
WEST = -1

splits = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
}

mirrorslash = {
    NORTH: EAST,
    EAST: NORTH,
    SOUTH: WEST,
    WEST: SOUTH,
}

mirrorbackslash = {
    NORTH: WEST,
    WEST: NORTH,
    SOUTH: EAST,
    EAST: SOUTH,
}
def next_peek(beam):
    position, direction = beam
    peek = position + direction
    if peek not in grid:
        return

    match grid[peek]:
        case "|" if direction not in splits["|"]:
            for split_direction in splits["|"]:
                yield peek, split_direction
        case "-" if direction not in splits["-"]:
            for split_direction in splits["-"]:
                yield peek, split_direction
        case "/":
            yield peek, mirrorslash[direction]
        case "\\":
            yield peek, mirrorbackslash[direction]
        case _:
            yield peek, direction


def travel(start):
    seen = set()
    energized = set()
    beams = [start]

    while beams:
        next_beams = []
        for beam in beams:
            if beam in seen:
                continue
            seen.add(beam)
            if beam[0] in grid:
                energized.add(beam[0])
            next_beams += next_peek(beam)
        beams = next_beams

    return len(energized)

print(travel((-1, EAST)))

R = len(data)
C = len(data[0])

def around_edges(R, C):
    for row in range(R):
        yield WEST + row * SOUTH, EAST
        yield R * EAST + row * SOUTH, WEST

    for col in range(C):
        yield NORTH + col * EAST, SOUTH
        yield C * SOUTH + col * EAST, NORTH

max_energized = max(travel(start) for start in around_edges(R, C))
print(max_energized)

