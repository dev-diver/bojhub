import sys
from collections import deque
input = sys.stdin.readline
N,M=map(int,input().split())
G = [[*input().strip()] for _ in range(N)]

x=y=-1
find=False
for i in range(N):
  if(find):break
  for j in range(M):
    if(G[i][j]=="I"):
      x, y = i, j
      find=True
      break

Q = deque([(x,y)])
V = [[False]*M for _ in range(N)]
V[x][y] = True
directions = [(0,1),(0,-1),(1,0),(-1,0)]
cnt=0
while Q:
  x,y = Q.popleft()
  if(G[x][y]=="P"):
    cnt+=1
  for dx,dy in directions:
    nx,ny = x+dx,y+dy
    if(0<=nx<N and 0<=ny<M and G[nx][ny]!="X" and V[nx][ny]==False):
      Q.append((nx,ny))
      V[nx][ny]=True

if cnt>0:
  print(cnt)
else:
  print("TT")