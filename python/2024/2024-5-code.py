data = open("inputs/2024-5.txt").read().split("\n\n")

comparisons, sequences = data
comparisons = set(comparisons.splitlines())
sequences = [[int(x) for x in sequence.split(",")]
    for sequence in sequences.splitlines()
]

def bubble_sort(sequence, comparisons):
    def swap(a, b):
        sequence[a], sequence[b] = sequence[b], sequence[a]

    N = len(sequence)
    sequence = sequence[:]
    for iteration in range(N):
        for pointer in range(1, N - iteration):
            swap_comparison = f"{sequence[pointer]}|{sequence[pointer - 1]}"
            if swap_comparison in comparisons:
                swap(pointer, pointer - 1)

    return sequence

def middle(sequence):
    mid = len(sequence) // 2
    return sequence[mid]

total_valid_middle = sum(middle(sequence)
    for sequence in sequences
    if bubble_sort(sequence, comparisons) == sequence
)

total_sorted_middle = sum(middle(sorted_sequence)
    for sequence in sequences
    for sorted_sequence in [bubble_sort(sequence, comparisons)] 
    if sorted_sequence != sequence
)

print(total_valid_middle, total_sorted_middle)
