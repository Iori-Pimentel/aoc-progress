data = open("inputs/2020-5.txt").read().splitlines()

binary = str.maketrans("FBRL", "0110")
source = [line.translate(binary) for line in data]
source = [(int(line[:7], base=2), int(line[7:], base=2)) for line in source]
max_id = max(row*8 + col for row, col in source)
print(max_id)
