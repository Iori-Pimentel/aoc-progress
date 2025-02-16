import re
from functools import lru_cache
from collections import Counter
data = open("inputs/2017-7.txt").read().splitlines()

def parse(line):
    return re.findall(r"\w+", line)

parent_to_children = dict()
node_to_weight = dict()
all_parents = set()
all_children = set()

for parent, recursive_weight, *children in map(parse, data):
    parent_to_children[parent] = children
    node_to_weight[parent] = int(recursive_weight)

    all_parents.add(parent)
    all_children |= set(children)

root = (all_parents - all_children).pop()
print(root)

@lru_cache
def recursive_weight(parent):
    return node_to_weight[parent] + sum(recursive_weight(child)
        for child in parent_to_children[parent]
    )

current = root
while parent_to_children[current]:
    weights = Counter(recursive_weight(child)
        for child in parent_to_children[current]
    )

    if len(weights) == 1:
        delta = correct_weight - wrong_weight
        correct_change = node_to_weight[current] + delta
        break

    (correct_weight, _), (wrong_weight, _) = weights.most_common()

    current = next(child
        for child in parent_to_children[current]
        if recursive_weight(child) == wrong_weight
    )

print(correct_change)
