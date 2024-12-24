import os
import pprint
from collections import Counter

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

lines = input.split("\n")

sum = 0
sum2 = 0
for line in lines:
    words = line.split()
    words_count = Counter(words)
    words = [sorted(word) for word in words]
    sum = sum + all(count == 1 for count in words_count.values())

    no_anagrams = all(words[i] != words[j] for i in range(len(words)) for j in range(i + 1, len(words)))
    sum2 = sum2 + (all(count == 1 for count in words_count.values()) and no_anagrams)

print(sum)
print(sum2)
