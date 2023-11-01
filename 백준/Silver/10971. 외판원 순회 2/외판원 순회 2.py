import sys
import copy
input = sys.stdin.readline
N=int(input())
M=[list(map(int,input().split())) for _ in range(N)]

MAX=1e9
def minCost(order,visitCity,visit): # 첫번째 순서로 visitCity 번 도시 방문
    if memo[order][visitCity]!=-1:
        return memo[order][visitCity]
    if order == len(visit)-1: # 현재 도시가 마지막 도시인 경우
            returnCost = M[visitCity][visit[0]] #다음 도시의 순회비용
            if returnCost == 0 : 
                r = MAX
                memo[order][visitCity] = r
                return r #순회를 못하는 경우
            else:
                r = returnCost
                memo[order][visitCity] = r
                return r #방문할 수 있는 경우 순회까지 더함
    cost = MAX
    for k in range(len(visit)): ## 다음 노드 탐색
        visitCost = M[visitCity][k] ## 방문비용
        if((k in visit) or visitCost==0) : continue  #이미 방문했거나 못 가는 경우 패스
        visit[order+1]=k
        cost = min(cost,visitCost + minCost(order+1,k,copy.copy(visit))) # 방문할 수 있고, 마지막이 아닌 경우 
    ans = cost
    return ans

result = []
visit=[-1]*N
memo = [[-1]*N for _ in range(N)]
visit[0]=0
print(minCost(0,0,copy.copy(visit)))