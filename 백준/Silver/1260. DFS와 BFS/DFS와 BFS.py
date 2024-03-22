import sys
from collections import deque
input = sys.stdin.readline
N,M,V= [*map(int,input().split())]
E = {e:[] for e in range(1,N+1)}
for _ in range(M):
    w,y = map(int,input().split())
    E[w]+=[y]
    E[y]+=[w]

for e in E:
    E[e].sort()

def dfs(node):
    ans=[]
    visit=[False]*(N+1)
    stack =[node]
    while stack:
        v = stack.pop()
        if visit[v]: continue
        visit[v]=True
        ans.append(v)
        for child in reversed(E[v]):
            stack.append(child)
    return ans

def bfs(node):
    ans=[]
    visit=[False]*(N+1)
    q=deque([node])
    while q:
        v = q.popleft()
        if visit[v]: continue
        visit[v] = True
        ans.append(v)
        for child in E[v]:
                q.append(child)
    return ans

print(*dfs(V))
print(*bfs(V))