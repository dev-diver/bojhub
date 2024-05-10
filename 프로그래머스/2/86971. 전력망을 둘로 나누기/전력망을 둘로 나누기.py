def solution(n, wires):
    G = {e:[] for e in range(1,n+1)}
    for v, u in wires:
        G[v].append(u)
        G[u].append(v)
        
    def dfs(V, cut):
        visited = [False]*(n+1)
        visited[V] = True
        visited[cut] = True
        stk=[V]
        while(stk):
            v = stk.pop()
            for nextV in G[v]:
                if(not visited[nextV]):
                    visited[nextV] = True
                    stk.append(nextV)
        return sum(1 for x in visited if x)-1
        
    mn = n
    for v1,v2 in wires:
        temp = abs(n-2*dfs(v1,v2))
        mn = min(mn, temp)
    return mn