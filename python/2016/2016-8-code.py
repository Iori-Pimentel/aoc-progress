from itertools import product
data = open("inputs/2016-8.txt").read().splitlines()

lights = [[0] * 50 for _ in range(6)]

for line in data:
    match line.split():
        case ["rect", xy]:
            xs, ys = xy.split("x")
            xs, ys = range(int(xs)), range(int(ys))
            for x, y in product(xs, ys):
                lights[y][x] = 1
        case ["rotate", "column", position, "by", offset]:
            position = position.removeprefix("x=")
            position, offset = int(position), int(offset)
            lights = [list(x) for x in zip(*lights)]
            lights[position] = lights[position][-offset:] + lights[position][:-offset]
            lights = [list(x) for x in zip(*lights)]
        case ["rotate", "row", position, "by", offset]:
            position = position.removeprefix("y=")
            position, offset = int(position), int(offset)
            lights[position] = lights[position][-offset:] + lights[position][:-offset]

print(sum(map(sum, lights)))
print(*lights, sep="\n")







