from functools import lru_cache
from operator import and_, or_, lshift, rshift
data = open("inputs/2015-7.txt").read().splitlines()

eq = " -> "
source = {
    line.split(eq)[1]:line.split(eq)[0].split()
    for line in data
}
operations = { "AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift }

@lru_cache
def solve(signal):
    try:
        return int(signal)
    except ValueError: pass

    try:
        left, opcode, right = source[signal]
        return operations[opcode](solve(left), solve(right))
    except ValueError: pass

    try:
        _not, right = source[signal]
        return ~solve(right)
    except ValueError: pass

    signal = source[signal][0]
    return solve(signal)

a_signal = solve("a")
solve.cache_clear()

source["b"] = [a_signal]
b_signal = solve("a")

print(a_signal)
print(b_signal)
