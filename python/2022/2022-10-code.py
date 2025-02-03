def run_instructions(screen):
    cycles, register = 0, 1
    for instruction in open("inputs/2022-10.txt"):
        match instruction.split():
            case ["addx", argument]:
                steps, delta = 2, int(argument)
            case ["noop"]:
                steps, delta = 1, 0

        for _ in range(steps):
            row, col = divmod(cycles, 40)
            if col in [register-1, register, register+1]:
                screen[row][col] = "#"

            cycles += 1

            if cycles in [20, 60, 100, 140, 180, 220]:
                yield cycles * register

        register += delta

screen = [list(" " * 40) for _ in range(6)]
print(sum(run_instructions(screen)))
print(*["".join(line) for line in screen], sep="\n")
