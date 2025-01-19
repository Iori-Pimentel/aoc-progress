from itertools import groupby
data = open("inputs/2015-10.txt").readline().strip()

def look_and_say(input, loop):
    for _ in range(loop):
        input = "".join(f"{len(list(group))}{key}" for key, group in groupby(input))
    return input

string_part1 = look_and_say(data, 40)
string_part2 = look_and_say(string_part1, 10)
print(len(string_part1), len(string_part2))
