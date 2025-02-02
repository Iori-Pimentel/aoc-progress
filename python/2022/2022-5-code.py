import re
data = open("inputs/2022-5.txt").read().split("\n\n")

crates, instruction = data
crates = {id: [box for box in boxes if box.strip()][::-1]
    for *boxes, id in zip(*crates.splitlines()) if id.isdigit()
}
instruction = instruction.splitlines()

def solve(crates, instruction, direction):
    for line in instruction:
        repeat, a, b = re.findall(r"\d+", line)
        crates[b] += crates[a][-int(repeat):][::direction]
        del crates[a][-int(repeat):]
    return "".join(crate[-1] for crate in crates.values())

print(solve(crates, instruction, -1))
print(solve(crates, instruction, 1))
