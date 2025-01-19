from itertools import repeat
data = open("inputs/2015-11.txt").readline().strip()

def increment(password):
    while True:
        i = 1
        while password[-i] == "z":
            password[-i] = "a"
            i += 1

        password[-i] = chr(ord(password[-i])+1)
        yield password

is_valid_password = lambda password: all([
    any(ord(a) == ord(b)-1 == ord(c)-2 for a,b,c in zip(password[0:], password[1:], password[2:])),
    not any(invalid in password for invalid in "iol"),
    len({a for a,b in zip(password[0:], password[1:]) if a == b}) >= 2,
])

def increment_valid(password):
    yield from (password for password in increment(password) if is_valid_password(password))

start = increment_valid(list(data))
password_part1, password_part2 = "".join(next(start)), "".join(next(start))
print(password_part1, password_part2)
