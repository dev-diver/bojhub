import copy
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int, input().split())
I = [[*map(int,input().split())] for _ in range(N)]

directions = [(0,1),(0,-1),(1,0),(-1,0)]

def melt(coord):
  x,y = coord
  if(I[x][y]==0): return 0
  cnt = 0
  for dx,dy in directions:
    nx,ny = x+dx,y+dy
    if(I[nx][ny]==0):
      cnt+=1 
  return max(0,I[x][y]-cnt)

def meltAll():
  global I
  NI = copy.deepcopy(I)
  for i in range(1,N-1):
    for j in range(1,M-1):
      NI[i][j] = melt((i,j))
  I = copy.deepcopy(NI)

def countIceberg():
  V=copy.deepcopy(I)
  def bfs(coord):
    x,y = coord
    if(V[x][y]==0): return 0
    Q=deque([(x,y)])
    V[x][y]=0
    while Q:
      x,y = Q.popleft()
      for dx,dy in directions:
        nx,ny = x+dx, y+dy
        if(V[nx][ny]!=0):
          Q.append((nx,ny))
          V[nx][ny]=0
    return 1

  cnt=0
  for i in range(1,N-1):
    for j in range(1,M-1):
      cnt+=bfs((i,j))
      if(cnt > 1): return cnt
  return cnt

year = 0
iceberg = 0
while True:
  iceberg = countIceberg()
  if(iceberg!=1):
    break
  year+=1
  meltAll()

if(iceberg==0):
  print(0)
else:
  print(year)