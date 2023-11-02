import sys
input = sys.stdin.readline
N = int(input())
M = [[*map(int,input().split())] for _ in range(N)]
M.sort(key=lambda x:x[1])

align=[-1]*N
cls=[0]*N
for num,start,end in M:
    for i in range(N):
        if start >= cls[i]: #end보다 느리면
            ci = i
            break
    cls[ci]=end
    align[num-1] = ci+1
print(cls.index(0) if 0 in cls else N)
print(*align, sep="\n")
