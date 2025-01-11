from itertools import permutations
data = open("inputs/2017-2.txt").read().splitlines()

sum_biggest = sum(max(map(int, line.split())) for line in data)
sum_smallest = sum(min(map(int, line.split())) for line in data)

def find_match(numbers):
    return next(a // b for a, b in permutations(numbers, 2) if a % b == 0)

total_part1 = sum_biggest - sum_smallest
total_part2 = sum(find_match(map(int, line.split())) for line in data)
print(total_part1, total_part2)


