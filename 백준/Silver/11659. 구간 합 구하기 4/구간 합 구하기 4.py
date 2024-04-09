N,M=map(int,input().split())
*Num, = map(int,input().split())
S = [(*map(int,input().split()),) for _ in range(M)]
s = [0]*(N+1)
for i in range(1,N+1):
  s[i] = s[i-1] + Num[i-1]
res=[]
for k in range(M):
  i,j = S[k]
  res.append(s[j]-s[i-1])
print(*res,sep="\n")