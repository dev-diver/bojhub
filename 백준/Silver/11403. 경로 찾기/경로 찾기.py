import sys
input = sys.stdin.readline
N = int(input())
G = [[*map(int,input().split())] for _ in range(N)]
D = [[0]*N for _ in range(N)]

for i in range(N):
  D[i][i] = 0

for i in range(N):
  for j in range(N):
    if(G[i][j]!=0):
      D[i][j] = G[i][j]

for k in range(N):
  for i in range(N):
    for j in range(N):
      newD = D[i][k] + D[k][j]
      if(newD>1):
        D[i][j] = 1
        
for d in D:
  print(*d)