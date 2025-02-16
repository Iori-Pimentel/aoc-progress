from functools import cache
data = open("inputs/2024-11.txt").read()
source = [int(x) for x in data.split()]

@cache
def stone_blinks(stone, blinks):
    if blinks == 0:
        return 1

    blinks -= 1

    if stone == 0:
        return stone_blinks(1, blinks)
    elif len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        a, b = str(stone)[half:], str(stone)[:half]
        return stone_blinks(int(a), blinks) + stone_blinks(int(b), blinks)
    else:
        return stone_blinks(stone * 2024, blinks)

total_part1 = sum(stone_blinks(stone, 25) for stone in source)
total_part2 = sum(stone_blinks(stone, 75) for stone in source)
print(total_part1, total_part2)
