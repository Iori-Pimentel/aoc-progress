from itertools import groupby
data = open("inputs/2019-4.txt").read()

start, end = data.split("-")
start, end = int(start), int(end)

has_double = lambda check: any(check.count(char) > 1 for char in check)
non_decreasing = lambda check: all(a <= b for a, b in zip(check, check[1:]))
has_non_group_double = lambda check: any(len(list(group)) == 2 for _, group in groupby(check))

part1 = sum(1
    for i in range(start, end)
        if has_double(str(i))
        if non_decreasing(str(i))
)
part2 = sum(1
    for i in range(start, end)
        if has_non_group_double(str(i))
        if non_decreasing(str(i))
)
print(part1, part2)
