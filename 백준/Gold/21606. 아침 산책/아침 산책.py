from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
F = [*map(int,[*input().strip()])]
inner = [*map(lambda x:x[0],filter(lambda x: x[1]==1,enumerate(F)))]
G = {i:[] for i in range(N)}
for _ in range(N-1):
  u,v = map(int,input().split())
  G[u-1].append(v-1)
  G[v-1].append(u-1)

def checkPath(s,e):
  stk = [(s,-1)]
  while(stk):
    v,p = stk.pop()
    if(v==e):
      return True
    if(v!=s and F[v]==1):
      continue
    for next_node in G[v]:
      if(next_node!=p):
        stk.append((next_node,v))
  return False

cnt=0
for s,e in combinations(inner,2):
  if checkPath(s,e):
    cnt+=1
print(cnt*2)