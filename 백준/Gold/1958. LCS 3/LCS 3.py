A=' '+input().strip()
B=' '+input().strip()
C=' '+input().strip()
dp = [[[0]*len(C) for _ in range(len(B))] for _ in range(len(A))]
for i in range(1,len(A)):
    for j in range(1,len(B)):
        for k in range(1,len(C)):
            if(A[i]==B[j] and B[j]==C[k]):
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
print(dp[-1][-1][-1])