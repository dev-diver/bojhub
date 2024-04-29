import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
G = [input().rstrip().split() for _ in range(N)]

T=[]
A=set()
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

def makeRoad():
    global A
    for x,y in T:
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            temp = []
            while(0<=nx<N and 0<=ny<N and G[nx][ny]!='T'):
                if(G[nx][ny]=='S'):
                    if(len(temp)==0):
                        return False
                    for t in temp:
                        A.add(t)
                    break
                else:
                    temp.append((nx,ny))
                    nx,ny = nx+dx,ny+dy
    return True

for i in range(N):
    for j in range(N):
        if(G[i][j]=='T'):
            T.append((i,j))

canTry = makeRoad()
if(canTry):
    success = False
    for comb in combinations(A,3):
        for x,y in comb:
            G[x][y] = 'O'
        success = isSuccess()
        if(success):
            break
        for x,y in comb:
            G[x][y] = 'X'
    print('YES' if success or len(A)<3 else 'NO')
else:
    print('NO')
