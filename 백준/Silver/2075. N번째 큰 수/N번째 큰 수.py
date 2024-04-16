import sys
import heapq
input = sys.stdin.readline
N = int(input())
Q=[-float('inf')]*N
for _ in range(N):
  *temp, = map(int,input().split())
  for e in temp:
    heapq.heappushpop(Q,e)
print(Q[0])