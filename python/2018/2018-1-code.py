from itertools import accumulate, cycle
data = open("inputs/2018-1.txt").read().splitlines()

frequencies = [int(line) for line in data]
seen = set()
seen_twice = next(freq
    for freq in accumulate(cycle(frequencies))
    if freq in seen or seen.add(freq)
)

print(sum(frequencies), seen_twice)
