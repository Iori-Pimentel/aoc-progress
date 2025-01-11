from hashlib import md5
from itertools import count
data = open("inputs/2015-4.txt").readline().strip()

def solve(data, target):
    for i in count():
        hex = md5(f"{data}{i}".encode()).hexdigest()

        if hex.startswith("0"*target):
            return i

target_5 = solve(data, 5)
target_6 = solve(data, 6)
print(target_5, target_6)
