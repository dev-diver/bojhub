from itertools import permutations
N,M = map(int,input().split())
*S, = map(int,input().split())
S.sort()

ans = set()
for c in permutations(map(str,S),M):
  c = ' '.join(c)
  if c not in ans:
    ans.add(c)

print(*ans,sep='\n')