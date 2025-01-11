data = open("inputs/2015-3.txt").readline()

def solve(data, players):
    directions = {"^": 1j, ">": 1, "v": -1j, "<": -1}
    positions = [0] * players

    visited = {0}
    for i, d in enumerate(data):
        positions[i % players] += directions[d]
        visited |= {positions[i % players]}

    return len(visited)

players_1 = solve(data, 1)
players_2 = solve(data, 2)
print(players_1, players_2)
