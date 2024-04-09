from collections import deque
M,N=map(int,input().split())
T=[[*map(int,input().split())] for _ in range(N)]

q=deque([])
for i in range(N):
  for j in range(M):
    if(T[i][j]==1):
      q.append((i,j,0))

minDay=0
directions=[(1,0),(-1,0),(0,1),(0,-1)]
while(q):
  i,j,day=q.popleft()
  minDay=max(minDay,day)
  for dx,dy in directions:
    nx,ny = i+dx,j+dy
    if(0<=nx<N and 0<=ny<M and T[nx][ny]==0):
      T[nx][ny]=1
      q.append((nx,ny,day+1))

flag=True
for i in range(N):
  if(not flag): break
  for j in range(M):
    if(T[i][j]==0):
      flag=False
      break

print(day if flag else -1)