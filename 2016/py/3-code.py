import os
import pprint

pprint = lambda *args: pprint.pprint(args, width = 100, compact = True)

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

triangles = input.split("\n")

valid_count = 0
for triangle in triangles:
    s1, s2, s3 = sorted(int(s) for s in triangle.split())

    if s1 + s2 > s3:
        valid_count = valid_count + 1

print(valid_count)

valid_count = 0
lines = input.split("\n")
for triangles_3 in [lines[i:i+3] for i in range(0,len(lines), 3)]:
    triangles_3 = [triangle.split() for triangle in triangles_3]
    triangles_3 = [list(triangle) for triangle in zip(*triangles_3)]

    for triangle in triangles_3:
        s1, s2, s3 = sorted(int(s) for s in triangle)

    if s1 + s2 > s3:
        valid_count = valid_count + 1

print(valid_count)
