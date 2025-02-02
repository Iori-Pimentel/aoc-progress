from string import ascii_letters
data = open("inputs/2022-3.txt").read().splitlines()

def parse(line):
    half = len(line) // 2
    return (line[:half], line[half:])

source = [parse(line) for line in data]
part1 = [next(a for a in ass if a in bss) for ass, bss in source]
source = data
part2 = [next(a for a in ass if a in bss and a in css)
    for ass, bss, css in zip(source[0::3], source[1::3], source[2::3])
]

print(sum(ascii_letters.index(char)+1 for char in part1))
print(sum(ascii_letters.index(char)+1 for char in part2))
