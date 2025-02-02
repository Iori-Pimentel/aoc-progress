data = open("inputs/2022-1.txt").read().split("\n\n")

source = sorted(sum(int(line) for line in elf.splitlines()) for elf in data)
print(source[-1], sum(source[-3:]))
