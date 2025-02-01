import re
data = open("inputs/2020-4.txt").read().split("\n\n")

checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
checks.pop(-1)
source = [dict(re.findall(r"([a-z]+):(\S+)", line)) for line in data]
total_part1 = sum(1
    for info in source
    if all(check in info for check in checks)
)
total_part2 = sum(1
    for info in source
    if all(check in info for check in checks)
    if int(info["byr"]) in range(1920, 2002+1)
    if int(info["iyr"]) in range(2010, 2020+1)
    if int(info["eyr"]) in range(2020, 2030+1)
    if ("cm" == info["hgt"][-2:] and int(info["hgt"][:-2]) in range(150, 193+1))
    or ("in" == info["hgt"][-2:] and int(info["hgt"][:-2]) in range(59, 76+1))
    if info["hcl"][0] == "#" and all(char in "abcdef0123456789" for char in info["hcl"][1:])
    if info["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if info["pid"].isdigit() and len(info["pid"]) == 9
)
print(total_part1, total_part2)
# print(source)
