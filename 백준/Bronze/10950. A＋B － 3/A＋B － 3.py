import sys
input = sys.stdin.readline
N = int(input())
M =[[*map(int,input().split())] for _ in range(N)]
r = []
for a,b in M:
    r.append(a+b)
print(*r,sep="\n")