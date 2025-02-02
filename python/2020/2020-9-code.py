from collections import deque
data = open("inputs/2020-9.txt").read().splitlines()

source = [int(x) for x in data]

def twosum(check, immediate):
    hash = set()
    for val in immediate:
        match = check - val
        if match in hash:
            return True
        hash.add(val)

immediate = deque(source[:25], maxlen=25)
for check in source[25:]:
    if not twosum(check, immediate):
        target = check
        break
    immediate.append(check)

print(target)

listing = deque()
for check in source:
    listing.append(check)
    if sum(listing) == target and len(listing) > 1:
        print("found")
        break

    while sum(listing) > target:
        listing.popleft()

    if sum(listing) == target and len(listing) > 1:
        print("found")
        break

print(min(listing) + max(listing))





