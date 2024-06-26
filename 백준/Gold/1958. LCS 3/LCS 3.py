import sys
input = sys.stdin.readline
A=input().rstrip()
B=input().rstrip()
C=input().rstrip()
lenA = len(A)+1
lenB = len(B)+1
lenC = len(C)+1
dp = [[[0]*lenC for _ in range(lenB)] for _ in range(lenA)]
for i in range(1,lenA):
    for j in range(1,lenB):
        for k in range(1,lenC):
            if(A[i-1]==B[j-1]==C[k-1]):
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
print(dp[-1][-1][-1])
