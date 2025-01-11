data = open("inputs/2017-1.txt").readline().strip()

half = len(data) // 2
sum_part1 = sum(int(x) for (x, y) in zip(data, data[1:] + data[0]) if x == y)
sum_part2 = sum(int(x) for (x, y) in zip(data, data[half:] + data[:half]) if x == y)
print(sum_part1, sum_part2)
