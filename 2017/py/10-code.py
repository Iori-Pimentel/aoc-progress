import os
import pprint

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

size = 256
knot = list(range(size))
start, skip = 0, 0
for length in [int(word) for word in input.split(",")]:
    for i in range(length // 2):
        a, b = (start + i) % size, (start + length - i) % size 
        knot[a], knot[b] = knot[b], knot[a]

    start = start + length + skip
    start = start % size
    skip = skip + 1

print(knot[0] * knot[1])

input = ""
size = 256
knot = list(range(size))
start, skip = 0, 0
for _ in range(64):
    for length in [ord(char) for char in input] + [17, 31, 73, 47, 23]:
        for i in range(length // 2):
            a, b = (start + i) % size, (start + length - i) % size 
            knot[a], knot[b] = knot[b], knot[a]

        start = start + length + skip
        start = start % size
        skip = skip + 1

knot = list(range(size))
print(knot)
chunk = 16
dense_hash = [0] * chunk
for i in range(chunk):
    for hash in knot[i * chunk:(i + 1) * chunk]:
        print(dense_hash[i], hash)
        dense_hash[i] = dense_hash[i] ^ hash

knot_hash = "".join([hex(hash)[2:] for hash in dense_hash])
print(knot_hash)
