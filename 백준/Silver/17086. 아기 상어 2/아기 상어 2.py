import sys
from collections import deque
input = sys.stdin.readline
N,M=map(int,input().split())
G = [[*map(int,input().split())] for _ in range(N)]
D = [[M+N]*M for _ in range(N)]
directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
def getSafe(coord):
    cx,cy = coord
    Q = deque([])
    Q.append((cx,cy,0))
    D[cx][cy] = 0
    result = 0
    while Q:
        x,y,dist = Q.popleft()
        result = dist
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if(0<=nx<N and 0<=ny<M and D[nx][ny]>dist+1 and G[nx][ny]!=1):
                D[nx][ny] = dist+1
                Q.append((nx,ny,dist+1))
    return result


for i in range(N):
    for j in range(M):
        if(G[i][j]==1):
            getSafe((i,j))

mx=0
for d in D:
    mx=max(mx,max(d))

print(mx)
