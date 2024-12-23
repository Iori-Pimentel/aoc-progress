import os

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

instructions = input.split("\n")

def solve(keypad, sx, sy):
    for instruction in instructions:
        cx, cy = sx, sy

        for char in instruction:
            dx, dy = {
                "U":(0, -1),
                "D":(0, 1),
                "L":(-1, 0),
                "R":(1, 0),
            }[char]

            cx, cy = cx + dx, cy + dy
            try:
                if cx < 0 or cy < 0:
                    cx, cy = cx - dx, cy - dy
                if keypad[cx][cy] == " ":
                    cx, cy = cx - dx, cy - dy
            except IndexError:
                cx, cy = cx - dx, cy - dy

        yield keypad[cy][cx]

keypad = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]
print("".join(solve(keypad, 1, 1)))

keypad = [
    [" ", " ", "1", " ", " "],
    [" ", "2", "3", "4", " "],
    ["5", "6", "7", "8", "9"],
    [" ", "A", "B", "C", " "],
    [" ", " ", "D", " ", " "],
]
print("".join(solve(keypad, 0, 2)))
