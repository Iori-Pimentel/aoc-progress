from collections import Counter
from string import ascii_uppercase
data = open("inputs/2023-7.txt").read().splitlines()

def cards_comparable(cards, hasJoker=False):
    order="23456789TJQKA"
    cards_frequency = Counter(cards)

    if hasJoker:
        order="J23456789TQKA"
        if "J" in cards and cards.strip("J"):
            joker = cards_frequency.pop("J")
            best = cards_frequency.most_common()[0][0]
            cards_frequency[best] += joker

    frequency = sorted(cards_frequency.values(), reverse=1)
    transform = str.maketrans(order, ascii_uppercase[:len(order)])
    cards_valued = cards.translate(transform)

    return frequency, cards_valued

def total(sorted_lines):
    return sum(rank * int(bid)
        for rank, (hand, bid) in enumerate(sorted_lines, 1)
    )

source = [line.split() for line in data]
sorted_jokerless = sorted(source, key=lambda line: cards_comparable(line[0]))
sorted_joker = sorted(source, key=lambda line: cards_comparable(line[0], True))
print(total(sorted_jokerless), total(sorted_joker))
