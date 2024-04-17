from itertools import permutations
N,M = map(int,input().split())
*S, = map(int,input().split())
S.sort()
for c in permutations(S,M):
  print(*c)