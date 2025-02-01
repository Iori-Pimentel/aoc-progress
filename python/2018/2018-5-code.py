from string import ascii_lowercase
data = open("inputs/2018-5.txt").read().strip()

source = list(data)
def shorten(source, ignore = ""):
    stack = []
    for token in source:
        if token.lower() == ignore.lower():
            continue
        if not stack:
            stack.append(token)
            continue

        switch = token.lower() if token.isupper() else token.upper()
        if stack[-1] == switch:
            stack.pop(-1)
        else:
            stack.append(token)

    return len(stack)

min_polymer = min(
    shorten(source, char)
    for char in ascii_lowercase
)
print(shorten(source), min_polymer)
