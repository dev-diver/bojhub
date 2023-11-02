import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))
N = int(input())
M = [[*map(int,input().split())] for _ in range(N)]

memo = [[-1]*N for _ in range(N)]
memo[N-1][N-1] = 1
def dfs(x,y): #x,y 에서 종착지까지 갈 수 있는 경우의 수
    if(x > N-1 or y > N-1):
        return 0
    elif(memo[x][y]!=-1):
        return memo[x][y]
    elif(M[x][y]==0):
        memo[x][y]=0
        return 0
    else:
        step = M[x][y]
        paths = dfs(x+step,y) + dfs(x,y+step)
        memo[x][y] = paths
        return paths
    
print(dfs(0,0))
