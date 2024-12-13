import re
machines = re.findall(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)', open('2024/Day 13/input.txt').read())
total = 0
for a_x, a_y, b_x, b_y, p_x, p_y in machines:
    a_x, a_y, b_x, b_y, p_x, p_y = map(int, [a_x, a_y, b_x, b_y, p_x, p_y])
    m = min((3*a + b for a in range(101) for b in range(101) if a*a_x + b*b_x == p_x and a*a_y + b*b_y == p_y), default=None)
    if m is not None:
        total += m
print(total)
