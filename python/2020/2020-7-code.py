import re
data = open("inputs/2020-7.txt").read().splitlines()

source = {re.search(r"\w+ \w+", line).group(): re.findall(r"(\d) (\w+ \w+) bag", line) for line in data}

def find(start, end="shiny gold"):
    return any(end == value or find(value) for _, value in source[start])

def count(bag):
    return sum(int(a) + int(a) * count(b) for a, b in source[bag])

total = sum(find(line) for line in source)

print(total, count("shiny gold"))
