from re import search
data = open("inputs/2016-4.txt").read().splitlines()

def parse(line):
    return search(r"(.*)-([0-9]+).(.+).", line).groups()

total_part1 = 0
match_part2 = "000"
for line in data:
    name, id, checksum = parse(line)
    id = int(id)

    ranking = sorted((-name.count(letter), letter) for letter in set(name))
    ranking = "".join(pair[1] for pair in ranking[:5])

    if sorted(ranking) == sorted(checksum):
        total_part1 += id

    def shift(char):
        shifted = (ord(char)-ord("a")+id) % 26
        return chr(shifted + ord("a"))

    if "northpole" in "".join(map(shift, name)):
        match_part2 = id

print(total_part1, match_part2)
