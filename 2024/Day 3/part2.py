import re
total=0
enabled=True
[(enabled:=True) if m.group(0)=='do()' else (enabled:=False) if m.group(0)=="don't()" else (total:=total + int(m.group(1))*int(m.group(2)) if enabled else total) for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', open('input.txt').read())] 
print(total)
