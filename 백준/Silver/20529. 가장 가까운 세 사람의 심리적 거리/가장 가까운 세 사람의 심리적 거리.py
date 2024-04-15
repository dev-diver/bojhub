import sys
from itertools import combinations
input = sys.stdin.readline

def calThree(A,B,C):
  a = set(A)
  b = set(B)
  c = set(C)
  return len(a-b)+len(b-c)+len(c-a)

T = int(input())

for _ in range(T):
  N = int(input())
  P = input().strip().split()

  if(N<=16):
    m = 12
    for k in combinations(P,3):
      m = min(m,calThree(*k))
    print(m)
    continue

  else:
    ans = 2
    d = {}
    for p in P:
      d[p] = d.get(p,0) + 1
      if d[p] >=3:
        ans = 0
        break
    print(ans)