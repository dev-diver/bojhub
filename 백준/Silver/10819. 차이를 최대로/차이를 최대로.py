import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
result = 0
def dfs(visited, res, idx, cnt):
    global n
    if cnt == n-1:
        return res
    maxRes=0
    for i in range(n):
        if not visited[i]:
            nextRes = res + abs(a[idx] - a[i])
            visited[i] = True
            maxRes = max(maxRes,dfs(visited,nextRes, i, cnt+1))
            visited[i] = False
    return maxRes


for i in range(n):
    visited = [False] * n
    visited[i] = True
    result = max(result, dfs(visited, 0, i, 0))
print(result)