N = int(input())
S = [i*i for i in range(1,318)]
dp = [0]*(N+1)
dp[1]=1
for i in range(2,N+1):
  mn=i
  for s in S:
    if(i-s<0):break
    mn = min(mn, 1 + dp[i-s])
  dp[i]=mn
print(dp[-1])