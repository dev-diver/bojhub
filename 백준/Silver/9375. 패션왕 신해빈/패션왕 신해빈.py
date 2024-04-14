import sys
input = sys.stdin.readline
T=int(input())
for _ in range(T):
  N = int(input())
  C = dict()
  for _ in range(N):
    w,c = input().strip().split()
    if c in C:
      C[c]+=1
    else:
      C[c]=1
  comb = 1
  for c in C:
    comb*=(C[c]+1)
  print(comb-1)