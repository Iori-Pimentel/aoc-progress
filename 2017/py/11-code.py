import os
import pprint
from collections import Counter

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

counter = Counter(input)
counter['n'], counter['s'] = max(0, counter['n'] - counter['s']), max(0, counter['s'] - counter['n'])
counter['w'], counter['e'] = max(0, (counter['w'] - counter['e']) // 2), max(0, (counter['e'] - counter['w']) // 2)


print(counter)
