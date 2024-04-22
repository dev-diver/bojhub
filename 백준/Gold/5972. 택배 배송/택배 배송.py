import sys,heapq,io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
N,M=map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for i in range(M):
  u,v,w = map(int,input().split())
  G[u].append(w<<16|v)
  G[v].append(w<<16|u)

D=[sys.maxsize]*(N+1)
D[1]=0
Q=[1]
while Q:
  q = heapq.heappop(Q)
  dist = q>>16
  n = q&0xffff
  if(D[n] < dist):
    continue
  for next in G[n]:
    w = next>>16
    v = next&0xffff
    distance = dist+w
    if(D[v] > distance):
      D[v] = distance
      heapq.heappush(Q,distance<<16|v)
print(D[-1])