import re
data = open("inputs/2017-9.txt").readline().strip()

no_negation = re.sub(r"!.", "", data)
garbage = sum(map(len, re.findall("<(.*?)>", no_negation)))
cleaned = re.sub(r"<.*?>|,", "", no_negation)

nesting, score = 0, 0
for char in cleaned:
    nesting += {"{": 1, "}": -1}[char]
    score += {"{": nesting, "}": 0}[char]

print(score, garbage)

