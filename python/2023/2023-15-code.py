data = open("inputs/2023-15.txt").read().strip().split(",")

def hashing(value):
    current = 0
    for char in value:
        current += ord(char)
        current *= 17
        current %= 256
    return current

total_part1 = sum(hashing(value) for value in data)
print(total_part1)
