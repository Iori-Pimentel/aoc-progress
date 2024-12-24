import os
import pprint

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

offsets = [int(line) for line in input.split("\n")]
index, steps = 0, 0
while index in range(len(offsets)):
    offsets[index] = offsets[index] + 1
    index = index + offsets[index] - 1
    steps = steps + 1

print(steps)

offsets = [int(line) for line in input.split("\n")]
index, steps = 0, 0
while index in range(len(offsets)):
    inc = -1 if offsets[index] >= 3 else 1
    offsets[index] = offsets[index] + inc
    index = index + offsets[index] - inc
    steps = steps + 1

# FIXME: taking too long
print(steps)
