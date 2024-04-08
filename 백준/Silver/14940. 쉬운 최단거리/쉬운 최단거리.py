from collections import deque
N,M = map(int,input().split())

R = []
start = (-1, -1)
for i in range(N):
  line = [*map(int,input().split())]
  if 2 in line:
    j = line.index(2)
    start = (i,j,0)
  R.append(line)

D = [[0 if m==0 else -1 for m in R[n]] for n in range(N)]

directions = [(0,1),(0,-1),(1,0),(-1,0)]
q = deque([start])
while(q):
  x, y, dist = q.popleft()
  if(R[x][y] == 0):
    continue
  R[x][y] = 0
  D[x][y] = dist
  for dx,dy in directions:
    nx,ny = x+dx,y+dy
    if(0<=nx<N and 0<=ny<M):
      q.append((nx,ny,dist+1))

for d in D:
  print(*d)