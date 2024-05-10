def solution(k, dungeons):
    
    visit=[False]*len(dungeons)
    def dfs(k,cnt):
        if(cnt>=len(dungeons)):
            return cnt
        result = cnt
        for i in range(len(dungeons)):
            need, cost = dungeons[i]
            if(visit[i]==False and k>=need):
                visit[i] = True  #visit 상태를 전달하지 않고 True, False만 Toggle
                result = max(result, dfs(k-cost,cnt+1))
                visit[i] = False
        return result

    mx = dfs(k,0)
    
    return mx