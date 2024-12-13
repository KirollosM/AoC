g=[line.strip() for line in open('2024/Day 13/input.txt')]
c=0
for i in range(1,len(g)-1):
    for j in range(1,len(g[0])-1):
        if g[i][j]=='A' and ((g[i-1][j-1]=='M' and g[i+1][j+1]=='S') or (g[i-1][j-1]=='S' and g[i+1][j+1]=='M')) and ((g[i-1][j+1]=='M' and g[i+1][j-1]=='S') or (g[i-1][j+1]=='S' and g[i+1][j-1]=='M')):
            c+=1
print(c)
