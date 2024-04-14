import sys
import heapq
input = sys.stdin.readline
N = int(input())
Q=[]

for _ in range(N):
  num = int(input())
  if(num==0):
    if(len(Q)>0):
      ab, n = heapq.heappop(Q)
      print(n)
    else:
      print(0)
  else:
    heapq.heappush(Q,(abs(num),num))