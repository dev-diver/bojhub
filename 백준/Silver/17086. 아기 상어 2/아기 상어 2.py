from collections import deque
N,M=map(int,input().split())
G = [[*map(int,input().split())] for _ in range(N)]

directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
def getSafe(coord):
    x,y = coord
    V=[[False]*M for _ in range(N)]
    Q=deque([])
    Q.append((x,y,0))
    V[x][y]=True
    while Q:
        x,y,dist = Q.popleft()
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if(0<=nx<N and 0<=ny<M and not V[nx][ny]):
                if(G[nx][ny]==1):
                    return dist+1
                V[nx][ny]=True
                Q.append((nx,ny,dist+1))

mx=0
for i in range(N):
    for j in range(M):
        if(G[i][j]!=1):
            safe = getSafe((i,j))
            mx=max(mx,safe)

print(mx)