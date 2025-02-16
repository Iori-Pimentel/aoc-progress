data = open("inputs/2017-11.txt").readline().strip()

clockwise = ["n", "ne", "se", "s", "sw", "nw"]

x, y, z = -1, 0, 1
directions = dict()
for rotation in clockwise:
    directions[rotation] = x, y, z
    x, y, z = -z, -x, -y

a, b, c = 0, 0, 0
alltime_distance = 0
distance = lambda a, b, c: sum(map(abs, [a, b, c])) // 2
for move in data.split(","):
    da, db, dc = directions[move]
    a, b, c = a+da, b+db, c+dc
    alltime_distance = max(alltime_distance, distance(a, b, c))

print(distance(a, b, c), alltime_distance)
