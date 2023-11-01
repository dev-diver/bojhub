import sys
import copy
input = sys.stdin.readline
N=int(input())
M=[list(map(int,input().split())) for _ in range(N)]
MAX=1e9
def minCost(order,visitCity,visit): # 첫번째 순서로 visitCity 번 도시 방문
    costs = [MAX]
    if order == len(visit)-1: # 현재 도시가 마지막 도시인 경우
            returnCost = M[visitCity][visit[0]] #다음 도시의 순회비용
            if returnCost == 0 : return MAX #순회를 못하는 경우
            return returnCost #방문할 수 있는 경우 순회까지 더함
    for k in range(len(visit)): ## 다음 노드 탐색
        visitCost = M[visitCity][k] ## 방문비용
        if((k in visit) or visitCost==0) : continue  #이미 방문했거나 못 가는 경우 패스
        visit[order+1]=k
        cost = visitCost + minCost(order+1,k,copy.copy(visit)) # 방문할 수 있고, 마지막이 아닌 경우 
        costs.append(cost)
    ans = min(costs)
    return ans

visit=[-1]*N
visit[0]=0
print(minCost(0,0,copy.copy(visit)))

#result = []
#visit=[-1]*N
#for city in range(N):
#    visit[0]=city
#    result.append(minCost(0,city,copy.copy(visit)))
# print(min(result))

