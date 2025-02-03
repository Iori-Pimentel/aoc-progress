import re
data = open("inputs/2022-4.txt").read().splitlines()

source = [[int(x) for x in re.findall(r"\d+", line)] for line in data]
source = [(set(range(s1,e1+1)), set(range(s2,e2+1)))  for s1, e1, s2, e2 in source]
part1 = [a<=b or b<=a for a, b in source]
part2 = [bool(a & b) for a, b in source]
print(sum(part1), sum(part2))
