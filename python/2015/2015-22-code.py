from itertools import product
import re
data = open("inputs/2015-22.txt").read()

# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

attacks = {
    "magic_missile": {
        "cost": 53,
        "attack": 4
    },
    "drain": {
        "cost": 73,
        "attack": 2,
        "heal": 2
    },
    "shield": {
        "cost": 113,
        "armor": 7 + 6j
    },
    "poison": {
        "cost": 173,
        "poison": 3 + 6j
    },
    "recharge": {
        "cost": 229,
        "mana_gain": 101 + 5j
    }
}

combinations = product(attacks.values(), repeat=5)

# returns: (player, boss, winner)

def fight(attacks, player, boss):
    for attack in attacks:
        do_attack()
        enemy_attack()
        if dead():
            yield winner
            continue

        for player, boss, winner in fight(attacks, player, boss):
            yield winner

player = {
    "health": 50,
    "damage": 0,
    "armor": 0,
    "mana_used": 0,
    "mana_gain": 0
}

boss = {
    "health": 50,
    "damage": 15,
}

boss = dict(for pair in zip(["health", "damage"], re.findall("[0-9]+", data)))
boss["poison"] = 0

for attack in combinations:
    print(attack)
