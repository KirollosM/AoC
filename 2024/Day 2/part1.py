s=0
for l in open('2024/Day 2/input.txt'):
    n=list(map(int,l.split()))
    inc=all(x<y for x,y in zip(n,n[1:]))
    dec=all(x>y for x,y in zip(n,n[1:]))
    dif=all(1<=abs(x-y)<=3 for x,y in zip(n,n[1:]))
    if (inc or dec) and dif: s+=1
print(s)
