import re
import math
data = open("inputs/2015-15.txt").read().splitlines()

def parse(line):
    return [int(values) for values in re.findall("-?[0-9]+", line)]

def score(recipe, combination, condition = lambda calories: True):
    recipe = [
            [property * amount for property in ingredient]
        for ingredient, amount in zip(recipe, combination)
    ]
    *properties, calories = [max(0, sum(property)) for property in zip(*recipe)]
    return {True: math.prod(properties), False: 0}[condition(calories)]

def combinator(target, size):
    if size == 1:
        yield [target]
        return

    for i in range(target+1):
        for subcombinations in combinator(target - i, size - 1):
            subcombinations.append(i)
            yield subcombinations

recipe = [parse(line) for line in data]
max_cookie_part1 = max(score(recipe, combination)
    for combination in combinator(100, 4)
)
max_cookie_part2 = max(score(recipe, combination, lambda calories: calories == 500)
    for combination in combinator(100, 4)
)
print(max_cookie_part1, max_cookie_part2)
