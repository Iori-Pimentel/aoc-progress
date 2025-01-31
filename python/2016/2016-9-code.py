from collections import deque
import re
data = open("inputs/2016-9.txt").read().strip()

tokens = [1 if char.isupper() else 0 for char in data]
markers = re.finditer("[x0-9]+", data)

referenced = set()
# TODO: clean
for mark in markers:
    if any(ref in range(mark.start(), mark.end()) for ref in referenced):
        continue

    length, repeat = mark.group().split("x")
    start = mark.end()+1
    length, repeat = int(length), int(repeat)

    for i in range(start, start+length):
        if tokens[i] == 0:
            referenced.add(i)
            tokens[i] = 1
        tokens[i] *= repeat

print(sum(tokens))

tokens = [1 if char.isupper() else 0 for char in data]
markers = re.finditer("[x0-9]+", data)
for mark in markers:
    length, repeat = mark.group().split("x")
    start = mark.end()+1
    length, repeat = int(length), int(repeat)

    for i in range(start, start+length):
        tokens[i] *= repeat

print(sum(tokens))
