import sys
from collections import deque
input = sys.stdin.readline
N,M = [*map(int,input().split())]  #N*M
R = [[*input().strip()] for _ in range(N)]

discovered = [[0]*M for _ in range(N)]
dist = [[0]*M for _ in range(N)]

q = deque()
discovered[0][0]=1
dist[0][0]=1
q.append((0,0))
while(q):
    x,y = q.popleft()
    # print("visit",x,y)
    if(x==N-1 and y==M-1):
        print(dist[x][y])
        break
    distance = dist[x][y]
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny = x+dx, y+dy
        if(0<=nx<N and 0<=ny<M and discovered[nx][ny]==0 and R[nx][ny]=='1'):
            # print("discovered",nx,ny)
            discovered[nx][ny]=1
            dist[nx][ny] = distance + 1
            q.append((nx,ny))