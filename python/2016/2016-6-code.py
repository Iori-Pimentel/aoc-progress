from collections import Counter
data = open("inputs/2016-6.txt").read().splitlines()

most_common = "".join(Counter(column).most_common(1)[0][0] for column in zip(*data))
least_common = "".join(Counter(column).most_common()[-1][0] for column in zip(*data))
print(most_common, least_common)
