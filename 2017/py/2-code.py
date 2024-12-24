import os
import pprint
import re

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

lines = input.split("\n")  

sum = 0
sum2 = 0
for line in lines:
    values = re.findall(r'[0-9]+', line)
    values = [int(value) for value in values]

    values.sort()

    sum = sum + values[-1] - values[0]
    for value in values:
        for value2 in values:
            if value2 % value == 0 and value != value2:
                sum2 = sum2 + (value2 // value)


print(sum)
print(sum2)
