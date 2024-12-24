import os
import pprint

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

sum = 0
for c1, c2 in zip(input, input[1:] + input[0]):
    if c1 == c2:
        sum = sum + int(c1)

print(sum)

sum = 0
half = len(input) // 2
for c1, c2 in zip(input, input[half:] + input[:half]):
    if c1 == c2:
        sum = sum + int(c1)

print(sum)
