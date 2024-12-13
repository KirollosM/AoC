l, r = zip(*[map(int, line.split()) for line in open('2024/Day 1/input.txt')])
print(sum(abs(a - b) for a, b in zip(sorted(l), sorted(r))))
