import os

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

floor = input.count("(") - input.count(")")
print(floor)

floor, count = 0, 0
for char in input:
    direction = {
        "(":1, ")":-1
    }
    floor = floor + direction[char]
    count = count + 1

    if floor < 0:
        print(count)
        break
