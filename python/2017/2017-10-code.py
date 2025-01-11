from itertools import batched
from functools import reduce
from operator import xor
data = open("inputs/2017-10.txt").readline().strip()

def twist(lengths, knot, pointer = 0, skip = 0):
    for length in lengths:
        for i in range(length//2):
            a, b = pointer+i, pointer+length-i
            a, b = a % len(knot), b % len(knot)
            print(a, b, pointer)
            knot[a], knot[b] = knot[b], knot[a]

        pointer += length + skip
        skip += 1

    return (knot, pointer, skip)

lengths = [int(x) for x in data.split(",")]
knot, _, _ = twist(lengths, [i for i in range(256)])
print(knot[0]*knot[1])

data = "1,2,4"
lengths = [ord(x) for x in data] + [17, 31, 73, 47, 23]
knot = [i for i in range(256)]
pointer, skip = 0, 0

for _ in range(64):
    knot, pointer, skip = twist(lengths, knot, pointer=pointer, skip=skip)

dense_hash = "".join(hex(reduce(xor, batch))[2:] for batch in batched(knot, 16))

print(dense_hash)
# TODO: continue

