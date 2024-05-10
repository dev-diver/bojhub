import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M = [*map(int,input().split())]
E = {e:[] for e in range(1,N+1)}
for _ in range(M):
    u,v = [*map(int,input().split())]
    E[u]+=[v]
    E[v]+=[u]
    
visit = [False]*(N+1)
def countLink(node):
    if visit[node] : return
    visit[node] = True
    # print(node,"방문")
    for nextNode in E[node]:
        countLink(nextNode)
    return

cnt=0
# print(E)
for i in range(1,N+1):
    # print(E[i])
    if not visit[i]:
        countLink(i)
        cnt+=1

print(cnt)