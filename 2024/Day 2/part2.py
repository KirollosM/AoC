s=0
for l in open('2024/Day 2/input.txt'):
    n=list(map(int,l.split()))
    def safe(m):
        inc=all(x<y for x,y in zip(m,m[1:]))
        dec=all(x>y for x,y in zip(m,m[1:]))
        dif=all(1<=abs(x-y)<=3 for x,y in zip(m,m[1:]))
        return (inc or dec) and dif
    if safe(n) or any(safe(n[:i]+n[i+1:]) for i in range(len(n))): s+=1
print(s)
