import sys
from collections import deque
MAX = 1000
input = sys.stdin.readline
R,C = [*map(int,input().split())] #R행 C열
M = [[*input().strip()] for _ in range(R)] # 물 시간 기록
wTime = [[MAX]*C for _ in range(R)]
gTime = [[-1]*C for _ in range(R)] #고슴도치 시간 기록
biber,gosm,water,empty,stone = "D","S","*",".","X"

wDscv=[[0]*C for _ in range(R)] #물 발견
gDscv=[[0]*C for _ in range(R)] #튈 경로 발견
wQ=deque()
gQ=deque()
for x in range(R):
    for y in range(C):
        if(M[x][y]==gosm):
            gQ.append((x,y))
            gTime[x][y] = 0
            gDscv[x][y] = 1
        if(M[x][y]==water):
            wQ.append((x,y))
            wTime[x][y] = 0
            wDscv[x][y] = 1

while(wQ):  # 물먼저 계산
    x,y = wQ.popleft()
    # print("time",wTime[x][y])
    newTime = wTime[x][y]+1
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny = x+dx,y+dy
        # print(nx,ny)
        if(0<=nx<R and 0<=ny<C and 
           wDscv[nx][ny]!=1 and
           M[nx][ny] not in [biber,stone]
           ):
            wDscv[nx][ny]=1
            wTime[nx][ny] = newTime
            wQ.append((nx,ny))

success = False
while(gQ):  # 고슴도치 계산
    x,y = gQ.popleft()
    # print(x,y, gTime[x][y])
    if M[x][y] == biber:
        print(gTime[x][y])
        success = True
        break
    newTime = gTime[x][y]+1
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny = x+dx,y+dy
        if(0<=nx<R and 0<=ny<C and 
           gDscv[nx][ny]!=1 and
           M[nx][ny] not in [stone,water] and
           newTime < wTime[nx][ny]
           ):
            gDscv[nx][ny] = 1
            gTime[nx][ny] = newTime
            gQ.append((nx,ny))

if not success:
    print("KAKTUS")