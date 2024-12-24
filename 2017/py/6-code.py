import os
import pprint

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

seen = dict()
state = input
steps = 0
while not state in seen:
    seen[state] = steps
    values = [int(value) for value in state.split("\t")]
    max_value = max(values)
    max_index = values.index(max_value)
    values[max_index] = 0

    for i in range(1, max_value + 1):
        i = (max_index + i) % len(values)
        values[i] = values[i] + 1

    state = "\t".join([str(value) for value in values])
    steps = steps + 1

print(steps)
print(steps - seen[state] )
