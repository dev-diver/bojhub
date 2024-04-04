import sys
input = sys.stdin.readline
N,M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]

STK = []

def dfs():
  cnt=0
  direction = [(0,1),(0,-1),(1,0),(-1,0)]
  while STK:
    x,y = STK.pop()
    if(A[x][y]==0):
      continue
    A[x][y]=0
    cnt+=1
    for dx,dy in direction:
      nx,ny = x+dx,y+dy
      if(0<=nx<N and 0<=ny<M and A[nx][ny]==1):
        STK.append((nx,ny))
  return cnt

cnt=0
s=0
for i in range(N):
  for j in range(M):
    if(A[i][j]==1):
      cnt+=1
      STK.append((i,j))
      s = max(s,dfs())

print(cnt)
print(s)
  