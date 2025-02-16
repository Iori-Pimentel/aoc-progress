import re
data = open("inputs/2024-7.txt").read().splitlines()

def combinator(numbers, part2):
    match numbers:
        case [last]:
            yield last
        case [*others, last]:
            for subtotal in combinator(others, part2):
                yield subtotal + last
                yield subtotal * last
                if part2:
                    yield int(f"{subtotal}{last}")
        case _:
            assert(0)

def parse(line):
    total, *numbers = map(int, re.findall(r"\d+", line))
    return total, numbers

total_part1 = sum(total
    for total, numbers in map(parse, data)
    if any(total == combinations for combinations in combinator(numbers, False))
)
total_part2 = sum(total
    for total, numbers in map(parse, data)
    if any(total == combinations for combinations in combinator(numbers, True))
)
print(total_part1, total_part2)
