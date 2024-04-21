import sys
import heapq
input = sys.stdin.readline
N,E = map(int,input().split())
K = int(input())
G = {i:[] for i in range(1,N+1)}
for _ in range(E):
  u,v,w = map(int,input().split())
  G[u].append((v,w))

D=[float('INF')]*(N+1)
D[K]=0
Q=[(0,K)]
while Q:
  dist, v = heapq.heappop(Q)
  if(dist > D[v]):
    continue
  for next_v,next_dist in G[v]:
    distance = dist + next_dist
    if(distance < D[next_v]):
      D[next_v] = distance
      heapq.heappush(Q,(distance,next_v))
*D, = map(lambda x:x if x!=float('inf') else 'INF', D[1:])
print(*D, sep='\n')