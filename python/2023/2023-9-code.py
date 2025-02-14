from itertools import pairwise

data = open("inputs/2023-9.txt").read().splitlines()
sequences = [[int(x) for x in line.split()] for line in data]

def next_sequence(sequence):
    if len(set(sequence)) == 1:
        return sequence[0]

    return sequence[-1] + next_sequence([b - a for a, b in pairwise(sequence)])

total_part1 = sum(map(next_sequence, sequences))
total_part2 = sum(next_sequence(sequence[::-1]) for sequence in sequences)
print(total_part1, total_part2)
