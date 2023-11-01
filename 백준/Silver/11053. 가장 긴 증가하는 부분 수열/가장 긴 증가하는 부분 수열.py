import sys
input = sys.stdin.readline

N = int(input())
*S, = map(int,input().split())
S = [0]+S
M = [0]*(N+1)

for i in range(N,-1,-1):
    r = 0
    for k in range(i+1,N+1):
        if(S[k]>S[i]):
            r = max(r, M[k])
    M[i]=r+1

print(M[0]-1)