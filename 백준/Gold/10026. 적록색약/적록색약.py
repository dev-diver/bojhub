import sys
from collections import deque
input = sys.stdin.readline
N=int(input())
M=[[*input().strip()] for _ in range(N)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(coord, vis,V):
  x,y = coord
  if(V[x][y]==True): return 0
  Q.append(coord)
  while Q:
    x,y = Q.popleft()
    for dx,dy in directions:
      nx,ny = x+dx,y+dy
      if(0<=nx<N and 0<=ny<N and V[nx][ny]==False and vis(M[x][y],M[nx][ny])):
        Q.append((nx,ny))
        V[nx][ny]=True
  return 1

def norm(init,cmp):
  return True if init==cmp else False

def abnorm(init,cmp):
  if(init=='B'):
    return True if init==cmp else False
  else:
    return False if cmp=='B' else True
  
Q=deque([])
normV=[[False]*N for _ in range(N)]
abnormV=[[False]*N for _ in range(N)]
normal=0
abnormal=0
for i in range(N):
  for j in range(N):
    normal+=bfs((i,j),norm,normV)
    abnormal+=bfs((i,j),abnorm,abnormV)
print(normal, abnormal)