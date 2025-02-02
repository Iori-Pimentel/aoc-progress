data = open("inputs/2022-2.txt").read().splitlines()

# TODO: refactor
def solve(line):
    enemy, player = line.split()
    enemy, player = "ABC".index(enemy), "XYZ".index(player)
    bonus = player + 1
    outcome = (player - enemy + 1) % 3 * 3
    return outcome + bonus

total = sum(solve(line) for line in data)
print(total)

def solve(line):
    enemy, outcome = line.split()
    enemy, outcome = "ABC".index(enemy), "XYZ".index(outcome)
    player = (outcome + enemy - 1) % 3
    bonus = player + 1
    outcome = outcome * 3
    return outcome + bonus

total = sum(solve(line) for line in data)
print(total)
# p-e-o = -1
