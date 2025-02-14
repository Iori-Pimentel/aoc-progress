data = open("inputs/2023-14.txt").read().splitlines()
def score(column):
    total, stable = 0, 0
    N = len(column)
    for position, char in enumerate(column):
        match char:
            case "O":
                total += N - stable
                stable += 1
            case "#":
                stable = position + 1

    return total

north_load = sum(score(column) for column in zip(*data))
print(north_load)

