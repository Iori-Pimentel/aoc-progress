data = open("inputs/2018-2.txt").read().splitlines()

counter = [{line.count(char) for char in line} for line in data]
total_part1 = sum(1 for count in counter if 2 in count) * sum(1 for count in counter if 3 in count)
print(total_part1)

for i in range(len(data[0])):
    new_data = [list(line) for line in data]
    for new in new_data:
        new[i] = ""
    counter = {new_data.count(new):new for new in new_data}

    if 2 in counter:
        print("".join(counter[2]))
        break

