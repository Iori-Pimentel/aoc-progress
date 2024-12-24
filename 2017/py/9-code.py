import os
import pprint

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

score , garbage = 0, 0
stack = list(input[:1])  # { < !
opposite = {"{":"}", "<":">"}
for char in input[1:]:
    if stack[-1] == "!":
        stack.pop()
    elif char == "!":
        stack.append("!")
    elif opposite[stack[-1]] == char:
        if char == "}":
            score = score + stack.count("{")
        stack.pop()
    elif stack[-1] != "<" and char != ",":
        stack.append(char)
    elif stack[-1] == "<":
        garbage = garbage + 1


print(score)
print(garbage)
