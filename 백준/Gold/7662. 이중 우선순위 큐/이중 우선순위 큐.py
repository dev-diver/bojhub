import sys, os, io
from array import array
from typing import Sequence
import heapq
from collections import defaultdict
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
T = int(input())
for _ in range(T):
  N = int(input())
  lQ = array('i')
  hQ = array('i')
  counter = defaultdict(int)
  for _ in range(N):
    cmd,n = input().split()
    n=int(n)
    if(cmd==b'I'):
      heapq.heappush(lQ,n) #type: ignore
      heapq.heappush(hQ,-n-1) #type: ignore
      counter[n]+=1
    if(cmd==b'D'):
      if(n==1):
        while hQ:
          elem = -heapq.heappop(hQ)-1 #type: ignore
          if(counter[elem]>0):
            counter[elem]-=1
            break
      else:
        while lQ:
          elem = heapq.heappop(lQ) #type: ignore
          if(counter[elem]>0):
            counter[elem]-=1
            break

  while(lQ and counter[lQ[0]]==0):
    heapq.heappop(lQ) #type: ignore
  while(hQ and counter[-hQ[0]-1]==0):
    heapq.heappop(hQ) #type: ignore
  if(hQ):
    print(-hQ[0]-1 , lQ[0])
  else:
    print("EMPTY")
