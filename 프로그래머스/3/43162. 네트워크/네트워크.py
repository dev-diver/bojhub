def solution(n, computers):
    
    stk = [(i,True) for i in range(n)]
    vis = [False for _ in range(n)]
    
    cnt = 0
    while stk:
        c, isRoot = stk.pop()
        if(vis[c]):
            continue  
        vis[c] = True
        if(isRoot):
            cnt += 1
            
        for next_c, conn in enumerate(computers[c]):
            if(conn==1):
                stk.append((next_c, False))
    
    return cnt