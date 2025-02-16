from collections import deque
from itertools import cycle
data = open("inputs/2024-9.txt").read().strip()

data = deque(data)
source = []
i = 0
source += [i] * int(data.popleft())
i += 1

while data:
    source += [None] * int(data.popleft())
    source += [i] * int(data.popleft())
    i += 1

source = deque(source)
score = 0
i = 0
while source:
    val = source.popleft()
    while val is None:
        val = source.pop()

    score += i * int(val)
    i += 1

print(score)
