import os
import pprint
import re
from collections import Counter

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

# aczupnetwp-mfyyj-opalcexpye-977[peyac]
lines = input.split("\n")

def solve(lines):
    for line in lines:
        values, sector, checksum = re.search(r'(.+)-([0-9]+).(.+)]', line).groups()
        sector = int(sector)
        values = "".join(values.split("-"))
        values = {(-values.count(char), ord(char)) for char in values}

        values = [char for count, char in sorted(values)[:5]]
        if all(ord(check) in values for check in checksum):
            yield sector

def solve2(lines):
    for line in lines:
        values, sector= re.search(r'(.+)-([0-9]+)', line).groups()
        sector = int(sector)
        def shift(char, amount):
            char = (ord(char) - ord("a") + sector)
            char = char % 26
            char = char + ord("a")
            return chr(char)

        values = "".join([shift(char, sector) for char in values])
        if "northpole" in values:
            return values, sector

print(sum(solve(lines)))
print(solve2(lines))
