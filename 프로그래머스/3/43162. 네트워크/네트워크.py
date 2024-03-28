def solution(n, computers):
    
    vis = [False for _ in range(n)]
    def dfs(c):
        if(vis[c]):
            return 0
        vis[c] = True
        for next_c, conn in enumerate(computers[c]):
            if(conn):
                dfs(next_c)
        return 1
    
    cnt = 0
    for i in range(n):
        cnt += dfs(i)
    
    return cnt