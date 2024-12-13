from collections import Counter
l, r = zip(*[map(int, line.split()) for line in open('2024/Day 1/input.txt')])
c = Counter(r)
print(sum(a * c[a] for a in l))
