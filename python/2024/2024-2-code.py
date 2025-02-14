from itertools import pairwise, combinations

data = open("inputs/2024-2.txt").read().splitlines()
source = [[int(x) for x in line.split()] for line in data]

def all_decreasing_or_increasing(numbers):
    return all(a > b for a, b in pairwise(numbers)) or all(a < b for a, b in pairwise(numbers))

def all_small_difference(numbers):
    return all(1 <= abs(a - b) <= 3 for a, b in pairwise(numbers))

def valid(numbers):
    return all_decreasing_or_increasing(numbers) and all_small_difference(numbers)

total_part1 = sum(1
    for numbers in source
    if valid(numbers)
)

total_part2 = sum(1
    for numbers in source
    if valid(numbers) or any(valid(subsequence)
        for subsequence in combinations(numbers, len(numbers) - 1)
    )
)

print(total_part1, total_part2)



