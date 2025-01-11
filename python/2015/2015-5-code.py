from re import findall
data = open("inputs/2015-5.txt").readlines()

is_nice_part1 = lambda line: (
    len(findall(r"[aeiou]", line)) >= 3 and
    len(findall(r"([a-z])\1", line)) > 0 and
    len(findall(r"ab|cd|pq|xy", line)) == 0
)

is_nice_part2 = lambda line: (
    len(findall(r"([a-z])([a-z]).*\1\2", line)) > 0 and
    len(findall(r"([a-z])[a-z]\1", line)) > 0
)

nice_part1 = sum(is_nice_part1(line) for line in data)
nice_part2 = sum(is_nice_part2(line) for line in data)
print(nice_part1, nice_part2)
