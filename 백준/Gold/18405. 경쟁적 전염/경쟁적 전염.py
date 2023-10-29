import sys
import heapq
input = sys.stdin.readline
N,K = map(int,input().split())
M = [[*map(int,input().split())] for _ in range(N)]
S,X,Y = map(int, input().split())

INF=int(1e9)
direct = [(1,0),(-1,0),(0,1),(0,-1)]

heap=[]
for x in range(N):
    for y in range(N):
        if(M[x][y]!=0):
            heapq.heappush(heap,(M[x][y],x,y))

for _ in range(S):
    next_virus = []
    while heap:
        cls,qx,qy = heapq.heappop(heap)
        for dx,dy in direct:
            nx,ny = qx+dx,qy+dy
            if(0<=nx<N and 0<=ny<N and M[nx][ny]==0):
                    M[nx][ny] = cls
                    next_virus.append((cls,nx,ny))
    for vir in next_virus: 
        heapq.heappush(heap, vir) 

print(M[X-1][Y-1])