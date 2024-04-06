import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int, input().split())
G = [[*map(int, input().strip())] for _ in range(N)]
D = [[[0,0] for _ in range(M)] for _ in range(N)]

q = deque([])
q.append(((0,0,0),1)) # (x,y,brk),dist
directions = [(0,1),(0,-1),(-1,0),(1,0)]
while(q):
  (x,y,brk),dist = q.popleft()
  if(x==N-1 and y==M-1):
    D[x][y][brk] = dist
    continue
  if(D[x][y][brk]!=0):
    continue
  D[x][y][brk] = dist
  for dx,dy in directions:
    nx,ny = x+dx,y+dy
    if(0<=nx<N and 0<=ny<M):
      if(G[nx][ny]==0 and D[nx][ny][brk]==0):
        q.append(((nx,ny,brk),dist+1))
      if(G[nx][ny]==1 and brk==0 and D[nx][ny][1]==0):
        q.append(((nx,ny,1),dist+1))

ans = D[N-1][M-1]
if(ans[0]==0 and ans[1]==0):
  print(-1)
elif(ans[0]==0 or ans[1]==0):
  print(max(ans))
else:
  print(min(ans))