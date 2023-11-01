import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

N = int(input())
T = [[*map(int,input().split())] for _ in range(N)]
T.sort(key=lambda x:(x[1],x[0]))

def maxC(m):
    end = T[m][1]
    k=m
    for i in range(m+1,N):
        if(T[i][0]>=end):
            k=i
            break
    if k!=m:
        return 1+maxC(k)
    return 0

print(maxC(0)+1)