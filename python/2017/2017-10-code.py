from itertools import batched
from functools import reduce
from operator import xor
data = open("inputs/2017-10.txt").read().strip()

def twist(twisters, iterations):
    size = 256
    pointer, skip = 0, 0
    knot = [node for node in range(size)]

    for _ in range(iterations):
        for twister in twisters:
            left = pointer
            right = pointer + twister - 1

            for _ in range(twister // 2):
                left, right = left % size, right % size
                knot[left], knot[right] = knot[right], knot[left]
                left, right = left + 1, right - 1

            pointer += twister + skip
            skip += 1

    return knot

values = [int(x) for x in data.split(",")]
knot = twist(values, 1)
print(knot[0] * knot[1])

values = [ord(x) for x in data] + [17, 31, 73, 47, 23]
knot = twist(values, 64)
dense_hash = "".join(hex(reduce(xor, batch))[2:].zfill(2)
    for batch in batched(knot, 16)
)
print(dense_hash)
