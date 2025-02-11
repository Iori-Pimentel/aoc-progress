data = open("inputs/2016-2.txt").read().splitlines()

keypad_part1 = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]
keypad_part2 = [
    [" ", " ", "1", " ", " "],
    [" ", "2", "3", "4", " "],
    ["5", "6", "7", "8", "9"],
    [" ", "A", "B", "C", " "],
    [" ", " ", "D", " ", " "],
]

directions = { "U": 1j, "D": -1j, "R": 1, "L": -1 }

def map_coordinates(array_2d):
    return {move: char
        for row, line in enumerate(array_2d)
        for col, char in enumerate(line)
        for move in [directions["D"]*row + directions["R"]*col]
        if not char.isspace()
    }

def solve(data, keypad, start):
    keypad = map_coordinates(keypad)

    def travel(line):
        position = start

        for move in line:
            position += directions[move]
            if not position in keypad:
                position -= directions[move]

        return keypad[position]

    return "".join(map(travel, data))

answer_part1 = solve(data, keypad_part1, -1j+1)  # start=keypad_5
answer_part2 = solve(data, keypad_part2, -2j+0)  # start=keypad_5
print(answer_part1, answer_part2)
