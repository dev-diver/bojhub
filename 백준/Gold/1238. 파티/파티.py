import sys
import heapq
input = sys.stdin.readline
N,M,X = map(int,input().split())
G = {i:{} for i in range(1,N+1)}
for _ in range(M):
  u,v,w = map(int, input().split())
  G[u][v] = w

def dijkstra(s):
  D = [float('inf')]*(N+1)
  D[s]=0
  Q = [(0,s)]
  while Q:
    dist,v = heapq.heappop(Q)
    if(dist>D[v]):
      continue
    for next_v,next_d in G[v].items():
      path_dist = dist+next_d
      if(path_dist < D[next_v]):
        D[next_v] = path_dist
        heapq.heappush(Q,(path_dist,next_v))
  return D

dist = dijkstra(X)
for i in range(1,X):
  D = dijkstra(i)
  dist[i] += D[X]
for i in range(X+1,N+1):
  D = dijkstra(i)
  dist[i] += D[X]

print(max(dist[1:]))