import os
import re

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

codes = input.split("\n")

diff = 0
for code in codes:
    diff = diff + 2
    pattern = r'\\(\\|")'
    diff = diff + len(re.findall(pattern, code))
    code = re.sub(pattern, "", code)

    pattern = r'\\x..'
    diff = diff + len(re.findall(pattern, code)) * 3

print(diff)

diff = 0
for code in codes:
    diff = diff + 2

    pattern = r'\\|"'
    diff = diff + len(re.findall(pattern, code))

print(diff)
