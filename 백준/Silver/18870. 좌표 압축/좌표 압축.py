N=int(input())
*X,=[(int(x),i) for i,x in enumerate(input().split())]
X.sort(key=lambda x:x[0])
ans = [-1]*N

k=-1
prev=1e9+1
for x,i in X:
  if(x!=prev):
    prev=x
    k+=1
  ans[i] = k
print(*ans)
