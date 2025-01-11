from functools import lru_cache
from operator import lt, le, gt, ge, eq, ne
data = open("inputs/2017-8.txt").read().splitlines()

operations = {"<":lt, "<=":le, ">":gt, ">=":ge, "==":eq, "!=": ne}
mult = {"inc":1, "dec":-1}

registers = {}
alltime_biggest = 0
for line in data:
    reg, op, chip, _if, a_reg, comp, b_val = line.split()
    registers.setdefault(reg, 0)
    registers.setdefault(a_reg, 0)
    b_val = int(b_val)

    if operations[comp](registers[a_reg], b_val):
        registers[reg] += int(chip) * mult[op]
        alltime_biggest = max(alltime_biggest, registers[reg])

biggest = max(registers.values())
print(biggest, alltime_biggest)
