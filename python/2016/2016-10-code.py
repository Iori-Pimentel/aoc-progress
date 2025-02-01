import re
from collections import defaultdict
data = open("inputs/2016-10.txt").read()

bots = {bot:{"low":0, "high": value, } for value, bot in re.findall("value ([0-9]+) goes to bot ([0-9]+)", data)}
# bots = defaultdict(int, bots)
relations = {bot:tuple(value) for bot, *value in re.findall("bot ([0-9]+) gives .* ([0-9]+) .* ([0-9]+)", data)}
