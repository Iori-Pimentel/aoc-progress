from collections import defaultdict
data = open("inputs/2015-17.txt").read().splitlines()

source = [int(x) for x in data]

basket = defaultdict(int)
for mask in range(1 << len(source)):
    total = [x for i, x in enumerate(source) if (1 << i & mask) != 0]
    if sum(total) == 150:
        basket[len(total)] += 1

print(sum(basket.values()), basket[min(basket)])
