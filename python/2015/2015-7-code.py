from functools import lru_cache
from operator import and_, or_, lshift, rshift, inv
data = open("inputs/2015-7.txt").read().splitlines()

eq = " -> "
source = {
    line.split(eq)[1]:line.split(eq)[0].split()
    for line in data
}
operations = { "AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift, "NOT": inv}

@lru_cache
def solve(signal):
    if type(signal) is int or signal.isdigit():
        return int(signal)

    match source[signal]:
        case *left, opcode, right:
            return operations[opcode](*[solve(arg) for arg in left + [right]])
        case [signal]:
            return solve(signal)

a_signal = solve("a")
solve.cache_clear()

source["b"] = [a_signal]
b_signal = solve("a")

print(a_signal)
print(b_signal)
