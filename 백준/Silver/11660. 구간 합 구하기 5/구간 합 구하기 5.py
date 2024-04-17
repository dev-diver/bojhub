import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G = [[*map(int,input().split())] for _ in range(N)]
S = [[0]*(N+1) for _ in range(N)]

for i in range(N):
  for j in range(1,N+1):
    S[i][j] = S[i][j-1] + G[i][j-1]

for _ in range(M):
  x1,y1,x2,y2 = map(lambda x:int(x)-1,input().split())
  s=0
  for x in range(x1,x2+1):
    k = S[x][y2+1]-S[x][y1]
    s+=k
  print(s)