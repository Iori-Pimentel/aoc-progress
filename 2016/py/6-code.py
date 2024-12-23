import os
import pprint

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

lines = input.split("\n")
columns= [list(column) for column in zip(*lines)]

def most_common(column):
    return sorted({(column.count(char), char) for char in column})[-1][1]

def least_common(column):
    return sorted({(column.count(char), char) for char in column})[0][1]

ans = [most_common(column) for column in columns]
print("".join(ans))

ans = [least_common(column) for column in columns]
print("".join(ans))
