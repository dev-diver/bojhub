import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
G = [input().rstrip().split() for _ in range(N)]

T=[]
A=[]
directions = [(1,0),(-1,0),(0,-1),(0,1)]

def isSuccess():
    for x,y in T:
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            while(0<=nx<N and 0<=ny<N and not G[nx][ny] in ['O','T']):
                if(G[nx][ny]=='S'):
                    return False
                nx,ny = nx+dx,ny+dy
    return True

for i in range(N):
    for j in range(N):
        if(G[i][j]=='T'):
            T.append((i,j))
        elif(G[i][j]=='X'):
            A.append((i,j))

success = False
for a,b,c in combinations(A,3):
    G[a[0]][a[1]] = 'O'
    G[b[0]][b[1]] = 'O'
    G[c[0]][c[1]] = 'O'
    success = isSuccess()
    if(success):
        break
    G[a[0]][a[1]] = 'X'
    G[b[0]][b[1]] = 'X'
    G[c[0]][c[1]] = 'X'
print('YES' if success else 'NO')
