import re
from functools import lru_cache
data = open("inputs/2017-7.txt").read().splitlines()

hierarchy = [re.findall(r"([a-z0-9]+)", line) for line in data]
weights = {line[0]:int(line[1]) for line in hierarchy}
children = {line[0]:line[2:] for line in hierarchy}
root = next(parent
    for parent in children.keys()
    if all(parent not in children for children in children.values())
)
wrong_weights = []
@lru_cache
def recursive_weight(parent):
    return weights[parent] + sum(map(recursive_weight, children[parent]))

print(root)
print(recursive_weight(root))
# TODO: Continue
