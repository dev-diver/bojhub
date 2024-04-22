import sys
from io import StringIO
import heapq
output = StringIO()
input = sys.stdin.readline
N,E = map(int,input().split())
K = int(input())
G = {i:[] for i in range(1,N+1)}
for _ in range(E):
  u,v,w = map(int,input().split())
  G[u].append(w<<16|v)

D=[sys.maxsize]*(N+1)
D[K]=0
Q=[K]
while Q:
  n = heapq.heappop(Q)
  dist = n>>16
  v = n&0xffff
  if(dist > D[v]):
    continue
  for next_n in G[v]:
    next_dist = next_n>>16
    next_v = next_n&0xffff
    distance = dist + next_dist
    if(distance < D[next_v]):
      D[next_v] = distance
      heapq.heappush(Q,distance<<16|next_v)
for x in D[1:]:
  if x!=sys.maxsize:
    output.write(f"{x}\n")
  else:
    output.write("INF\n")
sys.stdout.write(output.getvalue())