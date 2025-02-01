from itertools import takewhile, islice
import re
data = open("inputs/2016-9.txt").read().strip()

until = lambda iterable, end: "".join(takewhile(lambda char: char != end, iterable))
def decompress(iterable, recursive=False):
    unmarked = until(iterable, "(")
    length = until(iterable, "x")
    repeat = until(iterable, ")")
    if not length: return len(unmarked)

    length, repeat = int(length), int(repeat)
    marked = "".join(islice(iterable, length))

    if recursive:
        return len(unmarked) + decompress(iter(marked), recursive) * repeat + decompress(iterable, recursive)
    else:
        return len(unmarked) + len(marked) * repeat + decompress(iterable)

print(decompress(iter(data)))
print(decompress(iter(data), recursive=True))

tokens = [1 if char.isupper() else 0 for char in data]
markers = re.finditer("[x0-9]+", data)
for mark in markers:
    length, repeat = mark.group().split("x")
    start = mark.end()+1
    length, repeat = int(length), int(repeat)

    for i in range(start, start+length):
        tokens[i] *= repeat

print(sum(tokens))
