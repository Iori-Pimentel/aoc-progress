import re
from collections import Counter
from math import prod
from functools import reduce

games = [(game_id, played)
    for line in open("inputs/2023-2.txt")
    for game_id, played in [re.search(r"(\d+): (.+)", line).groups()]
    for game_id, played in [[int(game_id), played.split(";")]]
    for played in [[re.findall(r"(\d+) (\w+)", bags)
        for bags in played]]
    for played in [[Counter({color: int(count)
        for count, color in grabbed})
        for grabbed in played]]
]

available = Counter({"red": 12, "green": 13, "blue": 14})
valid_total = sum(game_id
    for game_id, played in games
    if all(available >= grabbed for grabbed in played)
)

union = lambda counters: reduce(lambda acc, c: acc | c, counters)
power_total = sum(prod(union(played).values())
    for _, played in games
)

print(valid_total, power_total)
