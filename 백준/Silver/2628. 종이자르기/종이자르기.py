import sys
input = sys.stdin.readline
X,Y = map(int, input().split())
N = int(input())
CUT = [[0,Y],[0,X]] # 가로 세로 바꿔서
for _ in range(N):
    ro,val = map(int,input().split())
    CUT[ro].append(val)
CUT[0].sort()
CUT[1].sort()

maxX = 0
maxY = 0
for i in range(len(CUT[0])-1):
    maxX=max(maxX,CUT[0][i+1]-CUT[0][i])
for i in range(len(CUT[1])-1):
    maxY=max(maxY,CUT[1][i+1]-CUT[1][i])
print(maxX*maxY)