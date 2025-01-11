from itertools import combinations
from operator import add, mul
data = open("inputs/2019-2.txt").readline()

operations = {1:add, 2:mul}
program = [int(x) for x in data.split(",")]

def solve(program, noun, verb):
    program = program[:]
    program[1], program[2] = noun, verb

    pointer = 0
    while program[pointer] != 99:
        op, x, y, out = program[pointer:pointer+4]
        x, y = program[x], program[y]
        pointer += 4
        program[out] = operations[op](x,y)

    return program[0]

answer_part1 = solve(program, 12, 2)
answer_part2 = next(
    100 * noun + verb
    for noun in range(100)
    for verb in range(100)
        if solve(program, noun, verb) == 19690720
)
print(answer_part1, answer_part2)


