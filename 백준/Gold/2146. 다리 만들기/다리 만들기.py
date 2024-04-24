import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
N = int(input())
M = [[*map(int,input().split())] for _ in range(N)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]
def getOutlines(coord):
  x,y = coord
  if(M[x][y]!=1): return []
  out = []
  Q = deque([coord])
  M[x][y]=2
  while Q:
    x,y = Q.popleft()
    isout = False
    for dx,dy in directions:
      nx,ny = x+dx,y+dy
      if(0<=nx<N and 0<=ny<N and M[nx][ny]!=2):
        if(M[nx][ny]==0):
          isout = True
        else:
          M[nx][ny]=2
          Q.append((nx,ny))
    if(isout):
      out.append((x,y))
  return out

def calDist(coordA, coordB):
  ax,ay = coordA
  bx,by = coordB
  dist = abs(ax-bx)+abs(ay-by)-1
  return dist

outlines = []
for i in range(N):
  for j in range(N):
    outline = getOutlines((i,j))
    if(outline):
      outlines.append(outline)

mn = N*2
for out1,out2 in combinations(outlines,2):
  for coordA in out1:
    for coordB in out2:
      dist = calDist(coordA,coordB)
      mn = min(mn,dist)
print(mn)