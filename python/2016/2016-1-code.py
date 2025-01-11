data = open("inputs/2016-1.txt").readline()

visited = {0j}
visited_multiple = []
position, facing = 0j, 1j
for moveset in data.split(", "):
    rotate, move = moveset[0], moveset[1:]
    facing *= {"R": -1j, "L": 1j}[rotate]

    for _ in range(int(move)):
        position += facing

        if position in visited:
            visited_multiple.append(position)

        visited.add(position)

manhattan_distance = lambda x: int(abs(x.imag) + abs(x.real))

print(manhattan_distance(position))
print(manhattan_distance(visited_multiple[0]))
