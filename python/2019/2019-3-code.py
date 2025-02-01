data = open("inputs/2019-3.txt").read().splitlines()

a, b = data
directions = { "U": 1j, "D": -1j, "R": 1, "L": -1 }

def travel(movement):
    position = steps = 0
    for direction, *distance in movement.split(","):
        direction, distance = directions[direction], int("".join(distance))
        for _ in range(distance):
            position += direction
            steps += 1
            yield (position, steps)

def manhattan_distance(number):
    return int(abs(number.imag) + abs(number.real))

a, b = dict(travel(a)), dict(travel(b))
intersection = set(a) & set(b)
closest_intersection = min(manhattan_distance(coords) for coords in intersection)
minimun_intersection = min(a[coords]+b[coords] for coords in intersection)
print(closest_intersection, minimun_intersection)

