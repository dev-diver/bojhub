import sys
input = sys.stdin.readline
N = int(input())
G  = {i:[] for i in range(1,N+1)}
for _ in range(1,N+1):
  *E, = map(int, input().split())
  i = E[0]
  j = 1
  while(E[j]!=-1):
    G[i].append((E[j],E[j+1]))
    j+=2

def dfs(u):
  V = [False]*(N+1)
  V[u] = True
  first_node = (0,u)
  stk = [first_node]
  max_n = first_node
  while stk:
    visit_node = stk.pop()
    dist, v = visit_node
    max_n = max(visit_node,max_n,key=lambda x:x[0])
    for next_v, to_dist in G[v]:
      if(not V[next_v]):
        stk.append((dist+to_dist,next_v))
        V[next_v] = True
  return max_n
end_leaf = dfs(1)[1]
print(dfs(end_leaf)[0])