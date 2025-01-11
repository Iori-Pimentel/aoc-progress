data = open("inputs/2017-5.txt").read().splitlines()


jumps = [int(x) for x in data]
pointer, increment = 0, 0
while pointer in range(len(data)):
    increment += 1
    jumps[pointer] += 1
    pointer += jumps[pointer] - 1

print(increment)

jumps = [int(x) for x in data]
pointer, increment = 0, 0
while pointer in range(len(data)):
    increment += 1
    mult = 1 if jumps[pointer] < 3 else -1
    jumps[pointer] += mult
    pointer += jumps[pointer] - mult

print(increment)
