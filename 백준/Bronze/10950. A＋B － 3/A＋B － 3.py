import sys
input = sys.stdin.readline
N = int(input())
r =[sum(map(int,input().split())) for _ in range(N)]
print(*r,sep="\n")