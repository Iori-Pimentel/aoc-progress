import re
from collections import defaultdict
data = open("inputs/2023-3.txt").read().splitlines()

numbers = [
    (int(number.group()), row, *number.span())
    for row, line in enumerate(data)
    for number in re.finditer(r"\d+", line)
]
symbols = {
    (row, number.start()): number.group()
    for row, line in enumerate(data)
    for number in re.finditer(r"[^\d.]", line)
}

def symbol_neighbours(row, start, end):
    neighbours = [(row_d, col_d)
        for row_d in [row-1, row, row+1]
        for col_d in range(start-1, end+1)
    ]
    return symbols.keys() & neighbours

total = sum(number
    for number, *position in numbers
    if symbol_neighbours(*position)
)

gears = defaultdict(list)
for number, *position in numbers:
    for symbol_position in symbol_neighbours(*position):
        if symbols[symbol_position] == "*":
            gears[symbol_position].append(number)

total_gears = sum(numbers[0] * numbers[1]
    for numbers in gears.values()
    if len(numbers) == 2
)

print(total, total_gears)
