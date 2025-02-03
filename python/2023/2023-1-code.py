import re
def digit(line):
    strings = [char for char in line if char.isdigit()]
    strings = int(str(strings[0] + strings[-1]))
    return strings

def digit_and_spelling(line):
    spelling = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits = re.findall(f"(?=([0-9]|{'|'.join(spelling)}))", line)
    strings = [str(spelling.index(digit)+1) if digit in spelling else digit for digit in digits]
    strings = int(str(strings[0] + strings[-1]))
    return strings

for parse in [digit, digit_and_spelling]:
    calibration = [parse(line) for line in open("inputs/2023-1.txt")]
    print(sum(calibration))
