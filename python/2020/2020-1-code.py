data = open("inputs/2020-1.txt").read().splitlines()

source = [int(x) for x in data]
hashmap = set()
for x in source:
    match = 2020-x
    if match in hashmap:
        print(x*match)
        break
    hashmap.add(x)

# TODO: recursion for n size
hashmap = set()
for x in source:
    for val in hashmap:
        match = 2020 - x - val
        if match in hashmap:
            print(x*match*val)
            break
    hashmap.add(x)
