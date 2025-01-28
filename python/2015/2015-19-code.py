import re
from collections import defaultdict
data = open("inputs/2015-19.txt").read()

# token ::= [A-Z][a-z]?
# molecule ::= token not (Rn | Y | Ar)
# transform ::= molecule " -> " molecule garbage[0] molecule garbage[1] garbage[2]
# garbage ::= Rn | (Y molecule){0,2} | Ar

lines, input = data.split("\n\n")
replacements = defaultdict(list)
for orig, repl in re.findall(r"(\w+) => (\w+)", lines):
    replacements[orig].append(repl)

tokens = re.findall("[A-Z][a-z]?", input)

unique = set()
for index, tok in enumerate(tokens):
    for repl in replacements[tok]:
        modified = tokens[:]
        modified[index] = repl
        unique.add("".join(modified))

start, end = len(["e"]), len(tokens)
garbage = tokens.count("Rn") + tokens.count("Ar") + tokens.count("Y") * 2
steps = end - start - garbage
print(len(unique), steps)
