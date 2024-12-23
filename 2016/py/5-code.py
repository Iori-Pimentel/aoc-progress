import os
import pprint
import hashlib

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

password = ""
count = 0
for _ in range(8):
    for i in range(10000000):
        string = input + str(count)
        count = count + 1
        hash = hashlib.md5(string.encode('utf-8')).hexdigest()

        if hash[:5] == "0" * 5:
            password = password + hash[5]
            break
print(password)

password = [None] * 8
count = 0
for _ in range(8):
    for i in range(10000000):
        string = input + str(count)
        count = count + 1
        hash = hashlib.md5(string.encode('utf-8')).hexdigest()

        if hash[:5] == "0" * 5:
            try:
                password[int(hash[5])] = password[int(hash[5])] or hash[6]
            except Error:
                pass
            break

print(password)
