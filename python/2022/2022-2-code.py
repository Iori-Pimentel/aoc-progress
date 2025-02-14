data = open("inputs/2022-2.txt").read().splitlines()

def parse(line):
    abc, xyz = line.split()
    return "ABC".index(abc), "XYZ".index(xyz)

get_outcome = lambda enemy, player: (player + 1 - enemy) % 3
enemy_player_total = sum(get_outcome(enemy, player) * 3 + player + 1
    for enemy, player in map(parse, data)
)

get_player = lambda enemy, outcome: (outcome - 1 + enemy) % 3
enemy_outcome_total = sum(outcome * 3 + get_player(enemy, outcome) + 1
    for enemy, outcome in map(parse, data)
)

print(enemy_player_total, enemy_outcome_total)
