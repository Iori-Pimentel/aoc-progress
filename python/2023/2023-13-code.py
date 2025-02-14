data = open("inputs/2023-13.txt").read().split("\n\n")
source = [pattern.splitlines() for pattern in data]

def finding(pattern):
    for mirror in range(1, len(pattern)):
        if all(pattern[before] == pattern[after]
            for offset in range(mirror)
            for before, after in [[mirror - offset - 1, mirror + offset]]
            if before >= 0 and after < len(pattern)
        ): return mirror

    return 0

def finding_mistake(pattern, mistake=1):
    for mirror in range(1, len(pattern)):
        if sum(sum(a != b for a, b in zip(pattern[before], pattern[after]))
            for offset in range(mirror)
            for before, after in [[mirror - offset - 1, mirror + offset]]
            if before >= 0 and after < len(pattern)
        ) == mistake: return mirror

    return 0

def find_mirror(pattern, func):
    rotated = ["".join(column) for column in zip(*pattern)]
    return func(pattern) * 100 or func(rotated)

total_part1 = sum(find_mirror(pattern, finding) for pattern in source)
total_part2 = sum(find_mirror(pattern, finding_mistake) for pattern in source)
print(total_part1, total_part2)
