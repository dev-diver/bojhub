import sys
import heapq
input = sys.stdin.readline

V,E = map(int, input().split())
G = {v:[] for v in range(1,V+1)}
for _ in range(E):
  u,v = map(int,input().split())
  G[u].append(v)
  G[v].append(u)

m = (0,float('inf'))
for s in range(1,V+1):
  D=[0]+[float('inf')]*V
  Q=[(0,s)]
  while Q:
    dist,u = heapq.heappop(Q)
    if(D[u]!=float('inf')):
      continue
    D[u] = dist
    for v in G[u]:
      heapq.heappush(Q,(dist+1,v))
  k = sum(D)
  m = min(m, (s,k), key=lambda x:x[1])
print(m[0])