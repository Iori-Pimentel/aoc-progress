data = open("inputs/2015-23.txt").read().splitlines()

tokens = [line.split() for line in data]

operations = {
    "hlf": lambda x: x // 2,
    "tpl": lambda x: x * 3,
    "inc": lambda x: x + 1,
    "jie": lambda x, offset: offset if x % 2 == 0 else 1,
    "jio": lambda x, offset: offset if x == 1 else 1,
}

for registers in [{"a": 0, "b": 0}, {"a": 1, "b": 0}]:
    pointer = 0
    while pointer in range(len(tokens)):
        match tokens[pointer]:
            case [instruction, offset] if instruction == "jmp":
                pointer += int(offset)
            case [instruction, identifier]:
                registers[identifier] = operations[instruction](registers[identifier])
                pointer += 1
            case [instruction, identifier, offset]:
                identifier = identifier.removesuffix(",")
                pointer += operations[instruction](registers[identifier], int(offset))
    print(registers)
