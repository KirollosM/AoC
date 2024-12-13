w='XMAS'
g=[line.strip() for line in open('2024/Day 13/input.txt')]
d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
c=0
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j]==w[0]:
            for di,dj in d:
                if all(0<=i+k*di<len(g) and 0<=j+k*dj<len(g[0]) and g[i+k*di][j+k*dj]==w[k] for k in range(1,4)):
                    c+=1
print(c)
