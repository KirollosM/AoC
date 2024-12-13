import re
m = re.findall(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)', open('2024/Day 13/input.txt').read())
t = 0
for ax, ay, bx, by, px, py in m:
    ax, ay, bx, by, px, py = map(int, [ax, ay, bx, by, px, py])
    px += 10000000000000
    py += 10000000000000
    D = ax * by - ay * bx
    if D == 0:
        continue
    n = ax * py - ay * px
    if n % D != 0:
        continue
    b = n // D
    if b < 0:
        continue
    a_num = px - b * bx
    if a_num % ax != 0:
        continue
    a = a_num // ax
    if a < 0 or a * ay + b * by != py:
        continue
    t += 3 * a + b
print(t)
