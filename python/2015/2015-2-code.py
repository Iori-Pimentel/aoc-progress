data = open("inputs/2015-2.txt").readlines()

dimensions = [sorted(map(int, line.split("x"))) for line in data]

paper = lambda a, b, c: 3*a*b + 2*a*c + 2*b*c
ribbon = lambda a, b, c: 2*a + 2*b + a*b*c

papers = sum(paper(a, b, c) for a, b, c in dimensions)
ribbons = sum(ribbon(a, b, c) for a, b, c in dimensions)

print(papers, ribbons)
