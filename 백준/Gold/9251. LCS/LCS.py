import sys
input = sys.stdin.readline
*A, = input().strip()
*B, = input().strip()
A=[0]+A
B=[0]+B

memo=[[0]*(len(B)) for _ in range(len(A))]
for i in range(len(A)):
    for j in range(len(B)):
        if not (i==0 or j==0):
            r=0
            if(A[i]==B[j]):
                r=1+memo[i-1][j-1]
            else:
                r=max(memo[i-1][j],memo[i][j-1])
            memo[i][j]=r
print(memo[len(A)-1][len(B)-1])
