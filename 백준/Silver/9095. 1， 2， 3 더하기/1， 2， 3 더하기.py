#dp
import sys
input = sys.stdin.readline
N = int(input())
T = [int(input()) for _ in range(N)]
maxT = max(T)

dp = [0]*(maxT+1)
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,maxT+1):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for t in T:
  print(dp[t])