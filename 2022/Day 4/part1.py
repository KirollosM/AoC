with open("2022/Day 4/input.txt", "r") as f:
    sections = f.readlines()

count = 0  

for pair in sections:
    pair = pair.strip()  
    p1, p2 = pair.split(",")
    
    start1, end1 = map(int, p1.split("-"))
    start2, end2 = map(int, p2.split("-"))
    
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
        count += 1

print(count)
