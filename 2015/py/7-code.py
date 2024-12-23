import os
import re

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read()

instructions = input.split("\n")

def solve(code):
    if code in cache:
        return cache[code]

    if code.isnumeric():
        cache[code] = code
        return code

    # 1-3 length
    codes = re.search('(.*) -> ' + code + r'\n', input).group(1).split()

    if len(codes) == 1:
        output = solve(codes[0])
    elif len(codes) == 2:
        output = ~solve(codes[1])
    else:
        operation = codes[1]
        val1, val2 = int(solve(codes[0])), int(solve(codes[2]))

        if operation == "AND":
            output = val1 & val2
        elif operation == "OR":
            output = val1 ^ val2
        elif operation == "RSHIFT":
            output = val1 >> val2
        elif operation == "LSHIFT":
            output = val1 << val2
        else:
            print("Wrong operation: " + operation)

    cache[code] = output
    return output

cache = {}
power = solve("a")
print(power)

cache = {}
cache["b"] = power
power = solve("a")
print(power)


