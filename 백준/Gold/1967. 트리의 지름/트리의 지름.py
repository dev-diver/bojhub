import sys
input = sys.stdin.readline
N = int(input())
G  = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
  *E, = map(int, input().split())
  G[E[0]].append((E[1],E[2]))
  G[E[1]].append((E[0],E[2]))

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