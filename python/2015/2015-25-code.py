import re
from itertools import islice
data = open("inputs/2015-25.txt").read()
def generate_code(code = 20151125):
    while True:
        yield code
        code = code * 252533 % 33554393

row, col = [int(x) for x in re.findall("[0-9]+", data)]
calculated_index = sum(range(row+col-1)) + col
print(next(islice(generate_code(), calculated_index - 1, calculated_index)))
