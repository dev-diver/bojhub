from itertools import combinations
N,M = map(int,input().split())
A = [i for i in range(1,N+1)]
for c in combinations(A,M):
  print(*c)