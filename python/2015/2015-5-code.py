from re import search
data = open("inputs/2015-5.txt").readlines()

is_nice_part1 = lambda line: all([
    search(r"([aeiou].*){3}", line),
    search(r"([a-z])\1", line),
    not search(r"ab|cd|pq|xy", line)
])

is_nice_part2 = lambda line: all([
    search(r"([a-z])([a-z]).*\1\2", line),
    search(r"([a-z])[a-z]\1", line)
])

nice_part1 = sum(is_nice_part1(line) for line in data)
nice_part2 = sum(is_nice_part2(line) for line in data)
print(nice_part1, nice_part2)
