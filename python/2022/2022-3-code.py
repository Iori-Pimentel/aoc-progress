from string import ascii_letters
from itertools import batched
data = open("inputs/2022-3.txt").read().splitlines()

def parse(line):
    half = len(line) // 2
    return line[:half], line[half:]

part1 = [next(a for a in ass if a in bss)
    for ass, bss in map(parse, data)
]
part2 = [next(a for a in ass if a in bss and a in css)
    for ass, bss, css in batched(data, 3)
]

print(sum(ascii_letters.index(char)+1 for char in part1))
print(sum(ascii_letters.index(char)+1 for char in part2))
