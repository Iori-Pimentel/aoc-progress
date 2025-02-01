data = open("inputs/2024-1.txt").read().splitlines()

source = [[int(x) for x in line.split()] for line in data]
a, b = zip(*source)
a, b = sorted(a), sorted(b)

sum_part1 = sum(abs(a - b)
    for a, b in zip(a, b)
)
sum_part2 = sum(a * b.count(a)
    for a in a
)
print(sum_part1, sum_part2)


