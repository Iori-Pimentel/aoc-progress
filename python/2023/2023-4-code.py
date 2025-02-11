import re
from functools import lru_cache

def numbers(string):
    return {int(x) for x in re.findall(r"\d+", string)}

scratchcards = [(numbers(card_id).pop(), wins)
    for line in open("inputs/2023-4.txt")
    for card_id, lottery, chosen in [re.split(r"[:|]", line)]
    for wins in [len(numbers(lottery) & numbers(chosen))]
]

points = sum(2 ** (wins-1)
    for _, wins in scratchcards
    if wins
)

def count(scratchcards):
    @lru_cache
    def counter(card_number, lottery):
        return 1 + sum(counter(c, l)
            for c, l in scratchcards[card_number:card_number+lottery]
        )

    return sum(counter(c, l) for c, l in scratchcards)

print(points, count(scratchcards))

