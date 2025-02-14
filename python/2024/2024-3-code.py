import re
data = open("inputs/2024-3.txt").read()

total_part1 = sum(int(a) * int(b)
    for a, b in re.findall(r"mul\((\d+),(\d+)\)", data)
)

enabled = True
total_part2 = 0
for val in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data):
    if val == "do()":
        enabled = True
    elif val == "don't()":
        enabled = False
    elif enabled:
        a, b = re.findall(r"\d+", val)
        total_part2 += int(a) * int(b)

print(total_part1, total_part2)
