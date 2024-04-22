import sys,heapq
input = sys.stdin.readline
N,M=map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for i in range(M):
  u,v,w = map(int,input().split())
  G[u].append((w,v))
  G[v].append((w,u))

D=[sys.maxsize]*(N+1)
D[1]=0
Q=[(0,1)]
while Q:
  dist,n = heapq.heappop(Q)
  if(D[n] < dist):
    continue
  for w,v in G[n]:
    distance = dist+w
    if(D[v] > distance):
      D[v] = distance
      heapq.heappush(Q,(distance,v))
print(D[-1])