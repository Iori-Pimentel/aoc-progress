import re
from functools import lru_cache

def numbers(string):
    return {int(x) for x in re.findall(r"\d+", string)}

scratchcards = [re.split(r"[:|]", line)
    for line in open("inputs/2023-4.txt")
]
scratchcards = [(numbers(card_number).pop(), len(numbers(lottery) & numbers(chosen)))
    for card_number, lottery, chosen in scratchcards
]

points = sum(1 << wins-1 if wins else 0
    for card_number, wins in scratchcards
)

def count(scratchcards):
    return sum(counter(c, l) for c, l in scratchcards)

@lru_cache
def counter(card_number, lottery):
    return 1 + sum(counter(c, l) for c, l in scratchcards[card_number:card_number+lottery])

print(points, count(scratchcards))

