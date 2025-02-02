from collections import deque

data = open("inputs/2022-6.txt").read()

def solve(size):
    window = deque(data[:size], maxlen=size)
    for index, char in enumerate(data[size:], size):
        if len(window) == len(set(window)):
            return index
        window.append(char)

print(solve(4), solve(14))
