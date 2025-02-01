import re
from itertools import groupby, islice, tee
from collections import defaultdict, Counter
data = open("inputs/2018-4.txt").read().splitlines()

source = sorted(data)
guards = defaultdict(Counter)
for line in source:
    if "Guard" in line:
        guard = int(line.split()[3][1:])
    elif "asleep" in line:
        asleep = int(line.split()[1][-3:-1])
    else:
        awake = int(line.split()[1][-3:-1])
        guards[guard] += Counter(range(asleep, awake))

total, max_guard = max(
    (sum(counter.values()), guard)
    for guard, counter in guards.items()
)
max_minute, _ = guards[max_guard].most_common(1)[0]
print(max_guard * max_minute)

total, max_guard = max(
    (max(counter.values()), guard)
    for guard, counter in guards.items()
)
max_minute, _ = guards[max_guard].most_common(1)[0]
print(max_guard * max_minute)
