import os
import pprint

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

lines = input.split("\n")

registers = dict()
lifetime_max = -999999999
for line in lines:
    reg, mode, value, _, check_reg, check_mode, check_val  = line.split()

    registers.setdefault(reg, 0)
    registers.setdefault(check_reg, 0)

    exec(f'check_cond = registers["{check_reg}"] {check_mode} {check_val}')
    if check_cond:
        mult = { "inc":1, "dec":-1 }[mode]
        registers[reg] = registers[reg] + int(value) * mult
        lifetime_max = max(lifetime_max, registers[reg])

print(max(registers.values()))
print(lifetime_max)
