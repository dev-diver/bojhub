A = ' '+input().strip()
B = ' '+input().strip()
dp = [[0]*len(B) for _ in range(len(A))]
for j in range(len(B)):
    dp[0][j] = 0
for i in range(1,len(A)):
    dp[i][0] = max(dp[i-1][0],1 if A[i]==B[0] else 0)
    for j in range(1,len(B)):
        if A[i]==B[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])