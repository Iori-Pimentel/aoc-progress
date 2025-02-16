import re
from collections import defaultdict
from itertools import batched
data = open("inputs/2016-10.txt").read()

bot = r"value (\d+) goes to bot (\d+)"
relation = r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)"

bots = defaultdict(list)
output = defaultdict(list)
groups = {"bot": bots, "output": output}

for given, bot in re.findall(bot, data):
    bots[bot].append(int(given))

relations = {bot: group_references
    for bot, *group_references in re.findall(relation, data)
}

while bots:
    for bot in list(bots.keys()):
        if len(bots[bot]) != 2:
            continue

        low, high = sorted(bots.pop(bot))
        if low == 17 and high == 61:
            print(bot)

        values = iter([low, high])
        for group, reference in batched(relations[bot], 2):
            groups[group][reference].append(next(values))

print(output["0"][0] * output["1"][0] * output["2"][0])
