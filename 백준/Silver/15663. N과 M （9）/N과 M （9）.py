from itertools import permutations
N,M = map(int,input().split())
*S, = map(int,input().split())
S.sort()

ans = []
for c in permutations(S,M):
  c = ' '.join([*map(str,c)])
  if(c not in ans):
    ans.append(c)

print(*ans,sep='\n')