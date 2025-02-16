from functools import cache
intructions = open("inputs/2016-12.txt").read().splitlines()

registers = {reg: 0 for reg in "abcd"}
pointer = 0
while pointer in range(len(intructions)):
    match intructions[pointer].split():
        case ["cpy", value, reg]:
            if value in registers:
                value = registers[value]
            registers[reg] = int(value)
        case ["inc", reg]:
            registers[reg] += 1
        case ["dec", reg]:
            registers[reg] -= 1
        case ["jnz", value, offset]:
            if value in registers:
                value = registers[value]
            if int(value) != 0:
                pointer += int(offset)
                continue

    pointer += 1

print(registers["a"])

