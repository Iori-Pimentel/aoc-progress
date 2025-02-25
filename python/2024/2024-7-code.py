import re
data = open("inputs/2024-7.txt").read().splitlines()

def combinator(inputs, part):
    *others, last = inputs
    if not others:
        yield last
        return

    for subtotal in combinator(others, part):
        yield subtotal + last
        yield subtotal * last
        if part == 2:
            yield int(f"{subtotal}{last}")

def parse(line):
    return map(int, re.findall(r"\d+", line))

for part in [1, 2]:
    total = sum(target
        for target, *inputs in map(parse, data)
        if target in combinator(inputs, part)
    )

    print(total)
