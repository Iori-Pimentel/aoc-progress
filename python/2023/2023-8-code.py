from itertools import cycle
import re
instructions, _,  *mappings = open("inputs/2023-8.txt")
instructions = cycle(instructions.strip())

mappings = {key: (left, right)
    for line in mappings
    for key, left, right in [re.findall("[A-Z]+", line)]
}

start, end = "AAA", "ZZZ"
steps = 0
current = start
for goto in instructions:
    if current == end:
        break
    current = mappings[current][{"L": 0, "R": 1}[goto]]
    steps += 1

print(steps)
