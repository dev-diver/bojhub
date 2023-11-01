import sys
input = sys.stdin.readline

N = int(input())
T = [[*map(int,input().split())] for _ in range(N)]
T.sort(key=lambda x:(x[1],x[0]))
end = 0
r=0
for Ts,Te in T:
    if Ts >= end:
        r+=1
        end=Te
print(r)