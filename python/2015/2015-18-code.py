from itertools import combinations
data = open("inputs/2015-18.txt").read().splitlines()

def neighbours(x, y):
    return sum((dx, dy) in lights
        for dy in [y-1, y, y+1]
        for dx in [x-1, x, x+1]
        if (dx, dy) != (x, y)
    )

for corners in [set(), {(0, 0), (0, 99), (99, 0), (99, 99)}]:
    lights = corners | {(x, y)
        for y, line in enumerate(data)
        for x, char in enumerate(line)
            if char == "#"
    }

    for _ in range(100):
        lights = corners | {(x, y)
            for y in range(100)
            for x in range(100)
            if (x, y) in lights and neighbours(x, y) in [2, 3]
            or (x, y) not in lights and neighbours(x, y) == 3
        }
    print(len(lights))
