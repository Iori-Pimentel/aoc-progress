data = open("inputs/2017-6.txt").readline().split()

shared_bank = [int(x) for x in data]

seen = {}
bank_hash = hash(tuple(shared_bank))
increment = 0
while bank_hash not in seen:
    seen[bank_hash] = increment
    increment += 1

    most = max(shared_bank)
    index = shared_bank.index(most)
    shared_bank[index] = 0
    while most > 0:
        index += 1
        index %= len(shared_bank)
        most -= 1
        shared_bank[index] += 1

    bank_hash = hash(tuple(shared_bank))

print(increment, increment - seen[bank_hash])


