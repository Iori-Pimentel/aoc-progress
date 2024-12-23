import os
import re

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

strings = input.split("\n")

is_nice_string_1 = lambda string: all([
    len(re.findall(r'[aeiou]', string)) >= 3,
    len(re.findall(r'([a-z])\1', string)) >= 1,
    len(re.findall(r'ab|cd|pq|xy', string)) == 0
])

is_nice_string_2 = lambda string: all([
    len(re.findall(r'([a-z])([a-z]).*\1\2', string)) > 0,
    len(re.findall(r'([a-z]).\1', string)) > 0,
])

count = sum(is_nice_string_1(string) for string in strings)
print(count)
count = sum(is_nice_string_2(string) for string in strings)
print(count)

