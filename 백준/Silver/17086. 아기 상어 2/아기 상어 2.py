import sys
from collections import deque
input = sys.stdin.readline
N,M=map(int,input().split())
G = [[*map(int,input().split())] for _ in range(N)]
V = [[False]*M for _ in range(N)]
directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
def getSafe(Q):
    result = 0
    while Q:
        x,y,dist = Q.popleft()
        result = dist
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if(0<=nx<N and 0<=ny<M and not V[nx][ny]):
                Q.append((nx,ny,dist+1))
                V[nx][ny]=True
    return result

Q=deque([])
for i in range(N):
    for j in range(M):
        if(G[i][j]==1):
            Q.append((i,j,0))
            V[i][j]=True
print(getSafe(Q))
