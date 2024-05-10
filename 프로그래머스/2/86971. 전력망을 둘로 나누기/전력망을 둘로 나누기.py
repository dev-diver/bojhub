def solution(n, wires):
    N = len(wires)+1
    T = [[False]*(N+1) for _ in range(N+1)]
    for u,v in wires:
        T[u][v] = True
        T[v][u] = True
        
    def dfs(V):
        visited=[False]*(N+1)
        visited[V]=True
        stk=[V]
        while stk:
            v = stk.pop()
            for i in range(1,N+1):
                if(T[v][i]==True and not visited[i]):
                    visited[i]=True
                    stk.append(i)
        result = sum(1 for x in visited if x)
        return result
    
    mn = N
    for u,v in wires:
        T[u][v] = False
        T[v][u] = False
        visit = dfs(1)
        temp = abs(N-2*visit)
        mn = min(mn, temp)
        T[u][v] = True
        T[v][u] = True
        
    return mn