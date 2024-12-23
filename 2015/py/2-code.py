import os

filename = os.getenv("inputfile")
with open(filename) as file:
    input = file.read().strip()

dimensions = input.split("\n")

sum_wrapping = 0
sum_ribbon = 0
for dimension in dimensions:
    lengths = [int(length) for length in dimension.split("x")]
    areas = [lengths[0] * lengths[1], lengths[1] * lengths[2], lengths[0] * lengths[2]]
    side_sums = [lengths[0] + lengths[1], lengths[1] + lengths[2], lengths[0] + lengths[2]]
    perimeters = [side_sum * 2 for side_sum in side_sums]
    volume = lengths[0] * lengths[1] * lengths[2]

    surface_area = sum([area * 2 for area in areas])
    sum_wrapping = sum_wrapping + surface_area + min(areas)

    sum_ribbon = sum_ribbon + min(perimeters) + volume

print(sum_wrapping)
print(sum_ribbon)
