import re
from itertools import product
data = open("inputs/2015-21.txt").read()

# Item: [Cost, Damage, Armor]
weapons = {
    "Dagger":     [ 8, 4, 0],
    "Shortsword": [10, 5, 0],
    "Warhammer":  [25, 6, 0],
    "Longsword":  [40, 7, 0],
    "Greataxe":   [74, 8, 0],
}
armors = {
    "Leather":    [ 13, 0, 1],
    "Chainmail":  [ 31, 0, 2],
    "Splintmail": [ 53, 0, 3],
    "Bandedmail": [ 75, 0, 4],
    "Platemail":  [102, 0, 5],
    None:         [  0, 0, 0],
}
rings = {
    "Damage +1":  [ 25, 1, 0],
    "Damage +2":  [ 50, 2, 0],
    "Damage +3":  [100, 3, 0],
    "Defense +1": [ 20, 0, 1],
    "Defense +2": [ 40, 0, 2],
    "Defense +3": [ 80, 0, 3],
    None:         [  0, 0, 0],
}

def fight(fighters):
    for i in range(2**64):
        attack, defend = i, i + 1
        attack, defend = attack % len(fighters), defend % len(fighters)

        damage_dealt = max(fighters[attack]["damage"] - fighters[defend]["armor"], 1)
        fighters[defend]["health"] -= damage_dealt

        if fighters[defend]["health"] <= 0:
            return fighters[attack]

boss_values = [int(x) for x in re.findall("[0-9]+", data)]
min_win = 9999
max_lose = 0
combinations = product(weapons.values(), armors.values(), rings.values(), rings.values())
for bought in combinations:
    price, damage, armor = (sum(values) for values in zip(*bought))

    player = {
        "health": 100,
        "damage": damage,
        "armor": armor,
    }
    boss = dict(zip(
        ["health", "damage", "armor"],
        boss_values
    ))

    if fight([player, boss]) == player:
        min_win = min(min_win, price)
    else:
        max_lose = max(max_lose, price)

print(min_win, max_lose)
