import sys
input = sys.stdin.readline
A = ' '+input().strip()
B = ' '+input().strip()
dps =[['']*len(B) for _ in range(len(A))]
for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i]==B[j]:
            dps[i][j]=dps[i-1][j-1]+A[i]
        else:
            maxs = ''
            if(len(dps[i-1][j]) > len(dps[i][j-1])):
                maxs = dps[i-1][j]
            else:
                maxs = dps[i][j-1]
            dps[i][j] = maxs
l=len(dps[-1][-1])
print(l)
if(l>0):
    print(dps[-1][-1])