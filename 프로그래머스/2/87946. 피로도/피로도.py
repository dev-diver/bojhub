def solution(k, dungeons):
    
    visit=[False]*len(dungeons)
    def dfs(k,cnt,dungeons):
        if(cnt>=len(dungeons)):
            return cnt
        result = cnt
        for i in range(len(dungeons)):
            need, cost = dungeons[i]
            if(visit[i]==False and k>=need):
                visit[i] = True
                result = max(result, dfs(k-cost,cnt+1,dungeons))
                visit[i] = False
        return result

    mx = dfs(k,0,dungeons)
    
    return mx