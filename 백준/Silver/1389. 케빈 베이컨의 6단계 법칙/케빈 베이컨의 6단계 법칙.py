import sys
input = sys.stdin.readline

V,E = map(int, input().split())
G = [[float('inf')]*V for _ in range(V)]

for _ in range(E):
  u,v = map(lambda x:int(x)-1, input().split())
  G[u][v] = 1
  G[v][u] = 1

D = [[float('inf')]*V for _ in range(V)]

for i in range(V):
  D[i][i] = 0

for u in range(V):
  for v in range(V):
    D[u][v] = G[u][v]

for k in range(V):
  for u in range(V):
    for v in range(V):
      newD = D[u][k] + D[k][v]
      if D[u][v] > newD:
        D[u][v] = newD

m = (0, float('inf'))
for i in range(V):
  m = min(m,(i+1,sum(D[i])), key=lambda x:x[1])
print(m[0])