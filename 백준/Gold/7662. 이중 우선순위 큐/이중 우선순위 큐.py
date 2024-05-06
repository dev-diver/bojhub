import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  N = int(input())
  lQ = []
  hQ = []
  counter = defaultdict(int)
  for _ in range(N):
    cmd,n = input().split()
    n=int(n)
    if(cmd=="I"):
      heapq.heappush(lQ,n)
      heapq.heappush(hQ,-n)
      counter[n]+=1
    if(cmd=="D"):
      if(n==1):
        while hQ:
          elem = -heapq.heappop(hQ)
          if(counter[elem]>0):
            counter[elem]-=1
            break
      else:
        while lQ:
          elem = heapq.heappop(lQ)
          if(counter[elem]>0):
            counter[elem]-=1
            break

  while(lQ and counter[lQ[0]]==0):
    heapq.heappop(lQ)
  while(hQ and counter[-hQ[0]]==0):
    heapq.heappop(hQ)
  if(hQ):
    print(-hQ[0] , lQ[0])
  else:
    print("EMPTY")
