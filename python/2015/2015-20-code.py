data = open("inputs/2015-20.txt").read()

target = int(data) // 10

def factors(x, limit=2**32):
    for i in range(int(x ** 0.5), 0, -1):
        if x % i == 0:
            yield i
            yield x // i
            limit -= 1
            if not limit:
                return

for i in range(1, target):
    presents = sum(factors(i))
    print(i, presents, target)
    if presents >= target:
        break

print(presents)
