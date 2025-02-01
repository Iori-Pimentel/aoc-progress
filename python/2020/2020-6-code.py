from collections import Counter
from itertools import groupby
from functools import reduce
data = open("inputs/2020-6.txt").read().splitlines()

def total(counters):
    result = Counter()
    for counter in counters:
        result += counter
    return result

def all_total(counters):
    return reduce(Counter.__and__, counters)

source = [Counter(line) for line in data]
source = [total(group) for key, group in groupby(source, key=lambda x: x == Counter()) if not key]
print(sum(len(counter) for counter in source))

source = [Counter(line) for line in data]
source = [all_total(group) for key, group in groupby(source, key=lambda x: x == Counter()) if not key]
print(sum(len(counter) for counter in source))


