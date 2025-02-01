import re
data = open("inputs/2020-2.txt").read().splitlines()

total_part1 = total_part2 = 0
for line in data:
    start, end, char, string = re.search(r"([0-9]+)-([0-9]+) (.): (.+)", line).groups()
    start, end = int(start), int(end)
    if start <= string.count(char) <= end:
        total_part1 += 1
    a, b = [index-1 < len(string) and string[index-1] == char for index in [start, end]]
    if a ^ b:
        total_part2 += 1
    
print(total_part1, total_part2)
