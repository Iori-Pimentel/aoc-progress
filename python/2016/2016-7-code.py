import re
data = open("inputs/2016-7.txt").read().splitlines()

addresses_split = [re.split("[^a-z]", line) for line in data]
supernets = [" ".join(address[0::2]) for address in addresses_split]
hypernets = [" ".join(address[1::2]) for address in addresses_split]

def is_abba(line):
    return any(a+b == d+c and a != b
        for a, b, c, d in zip(line, line[1:], line[2:], line[3:]))

def is_ababab(supernet, hypernet):
    return any(a == c and a != b and b+a+b in hypernet
        for a, b, c in zip(supernet[0:], supernet[1:], supernet[2:])
    )

count_part1 = sum(is_abba(supernet) and not is_abba(hypernet)
    for (supernet, hypernet) in zip(supernets, hypernets)
)
count_part2 = sum(is_ababab(supernet, hypernet)
    for (supernet, hypernet) in zip(supernets, hypernets)
)
print(count_part1, count_part2)


