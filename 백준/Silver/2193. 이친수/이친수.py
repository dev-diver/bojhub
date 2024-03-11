N=int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 0
dp[1] = 1

for i in range(2,N+1):
  dp[i] = sum(dp[0:i-1])+1

print(dp[N])