import sys
input = sys.stdin.readline
N =int(input())
M = [[*map(int,input().split())] for _ in range(N)]
S = [[-1]*N for _ in range(N)]
INF = int(1e9)

for i in range(N):
    S[i][i] = 0

for l in range(2,N+1):
    for i in range(N-l+1):
        j = i+l-1
        r = INF
        for k in range(i,j):
            newR = S[i][k]+S[k+1][j] + M[i][0]*M[k][1]*M[j][1]
            r = min(r,newR)
        S[i][j] = r

print(S[0][N-1])
