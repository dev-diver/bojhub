from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
F = [*input().strip()]
G = {i:[] for i in range(N)}
for _ in range(N-1):
  u,v = map(int,input().split())
  G[u-1].append(v-1)
  G[v-1].append(u-1)

def countPath(s):
  stk = [(s,-1)]
  cnt = 0
  while(stk):
    v,p = stk.pop()
    for next_node in G[v]:
      if(next_node!=p):
        if(F[next_node]=='1'):
          cnt+=1
        else:
          stk.append((next_node,v))
  return cnt

cnt = 0
for i in range(N):
  if(F[i]=='1'):
    cnt+=countPath(i)
print(cnt)