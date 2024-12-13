import re
print(sum(int(a)*int(b) for a,b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', open('input.txt').read())))
