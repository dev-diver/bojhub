import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

N = int(input())
*S, = map(int,input().split())
S = [0]+S
M = [0]*(N+1)

def lis(i):
    if M[i]!=0: return M[i]
    r=0
    for k in range(i+1,N+1):
        if(S[k]>S[i]):
            r = max(r,lis(k))
    r+=1
    M[i]=r
    return r

print(lis(0)-1)