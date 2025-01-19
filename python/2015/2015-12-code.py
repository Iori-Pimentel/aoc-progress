import re
import json
data = open("inputs/2015-12.txt").readline()

sum_part1 = sum(int(number) for number in re.findall(r"-?[0-9]+", data))

def sum_json(obj):
    match obj:
        case int():
            return obj
        case list():
            return sum(map(sum_json, obj))
        case dict() if "red" not in obj.values():
            return sum(map(sum_json, obj.values()))
        case _:
            return 0

print(sum_part1, sum_json(eval(data)))
