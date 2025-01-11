data = open("inputs/2017-4.txt").read().splitlines()

passphrases = [line.split() for line in data]

has_no_duplicates = lambda list: len(list) == len(set(list))
has_no_anagram = lambda list: has_no_duplicates(["".join(sorted(x)) for x in list])

count_no_duplicate = sum(map(has_no_duplicates, passphrases))
count_no_anagram = sum(map(has_no_anagram, passphrases))

print(count_no_duplicate, count_no_anagram)
