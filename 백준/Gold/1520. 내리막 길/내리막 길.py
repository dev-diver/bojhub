import sys
import heapq
input = sys.stdin.readline
M,N = map(int,input().split())
G = [[*map(int,input().split())] for _ in range(M)]
D = [[0]*N for _ in range(M)]
D[0][0]=1
Q = [(-G[0][0],0,0)]
directions = [(0,1),(0,-1),(1,0),(-1,0)]
while Q:
  H,x,y = heapq.heappop(Q)
  if(not (x==0 and y==0) and D[x][y]>0):
    continue
  H*=-1
  for dx,dy in directions:
    nx,ny = x+dx,y+dy
    if(0<=nx<M and 0<=ny<N):
      h = G[nx][ny]
      if(h<H):
        heapq.heappush(Q, (-h,nx,ny))
      elif(h>H):
        D[x][y]+=D[nx][ny]

print(D[M-1][N-1])