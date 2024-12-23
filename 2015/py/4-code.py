import os
import hashlib

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

def solve(zero_count):
    number = 1
    hash = ""
    while True:
        string = input + str(number)
        hash = hashlib.md5(string.encode('utf-8')).hexdigest()

        if hash[:zero_count] == "0" * zero_count:
            return number

        number = number + 1

print(solve(5))
print(solve(6))
