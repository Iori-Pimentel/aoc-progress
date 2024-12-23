import os

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

distances = input.split("\n")
end = distances[-1].split()[2]

airports = set(distance.split()[0] for distance in distances)
count = len(airports)

print(airports)
