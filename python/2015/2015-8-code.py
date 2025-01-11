data = open("inputs/2015-8.txt").read().splitlines()

count_part1 = sum(len(line) - len(eval(line)) for line in data)
count_part2 = sum(line.count("\"") + line.count("\\") + 2 for line in data)
print(count_part1, count_part2)
