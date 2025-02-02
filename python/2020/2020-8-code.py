data = open("inputs/2020-8.txt").read().splitlines()

source = [line.split() for line in data]
source = [(a, int(b)) for a, b in source]
def solve(pointer = 0, accumulator = 0):
    seen = set()
    while pointer in range(len(source)):
        if pointer in seen:
            return accumulator

        seen.add(pointer)
        match source[pointer]:
            case ["jmp", offset]:
                pointer += offset
            case ["acc", amount]:
                accumulator += amount
                pointer += 1
            case ["nop", amount]:
                pointer += 1

    return accumulator
print(solve())

def solve(pointer = 0, accumulator = 0, seen = set(), changed = False):
    while pointer in range(len(source)):
        found = pointer == len(source)-1
        if pointer in seen:
            return 0

        seen.add(pointer)
        match source[pointer]:
            case ["jmp", offset]:
                if not changed:
                    other = solve(pointer + 1, accumulator, seen.copy(), True)
                    if other: return other
                pointer += offset
            case ["acc", amount]:
                accumulator += amount
                pointer += 1
            case ["nop", amount]:
                if not changed:
                    other = solve(pointer + amount, accumulator, seen.copy(), True)
                    if other: return other
                pointer += 1
        if found:
            return accumulator

    return 0
print(solve())
