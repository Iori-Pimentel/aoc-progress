import os
import pprint
import re

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

lines = input.split("\n")


def pair(ip):
    abba = []
    not_abba = []
    curr_abba = abba
    for char in ip:
        if char in "[]":
            curr_abba.append("-")
            curr_abba = {
                "[": not_abba,
                "]": abba
            }[char]
            continue

        curr_abba.append(char)
    return abba, not_abba

def valid(check_abba):
    check_abba = "".join(check_abba)
    try:
        a, b = re.search(r'(.)(.)\2\1', check_abba).groups()
        return a != b
    except AttributeError:
        return None

valid_count = 0
for line in lines:
    abba, not_abba = pair(line)
    if valid(abba) and not valid(not_abba):
        valid_count = valid_count + 1

print(valid_count)
