from hashlib import md5
from itertools import count
data = open("inputs/2016-5.txt").readline().strip()

password_part1 = ""
password_part2 = ["0"] * 8

available = set("01234567")

for i in count():
    hex = md5(f"{data}{i}".encode()).hexdigest()
    checksum, first, second = hex[:5], hex[5], hex[6]

    if checksum == "0"*5:
        if len(password_part1) < 8:
            password_part1 += first

        if first in available:
            password_part2[int(first)] = second
            available.remove(first)

    if not available:
        break

print(password_part1, "".join(password_part2))
