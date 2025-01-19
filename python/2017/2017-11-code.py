data = open("inputs/2017-11.txt").readline().strip()

# TODO: comprehend
directions = {
    'n':  (0, 1, -1),
    'nw': (-1, 1, 0),
    'sw': (-1, 0, 1),
    's':  (0, -1, 1),
    'se': (1, -1, 0),
    'ne': (1, 0, -1),
}
a, b, c = 0, 0, 0
alltime_distance = 0
distance = lambda a, b, c: sum(map(abs, [a, b, c])) // 2
for move in data.split(","):
    da, db, dc = directions[move]
    a, b, c = a+da, b+db, c+dc
    alltime_distance = max(alltime_distance, distance(a, b, c))

print(distance(a, b, c), alltime_distance)
