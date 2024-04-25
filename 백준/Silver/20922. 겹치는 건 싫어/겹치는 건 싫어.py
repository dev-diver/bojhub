N,K = map(int,input().split())
*S, = map(int,input().split())
D = dict()
L = 0
maxL = 0
for i in range(N):
  s = S[i]
  cnt = D.get(s,0) +1
  if(cnt > K):
    maxL = max(L,maxL)
    while(D[s]+1>K):
      k = S[i-L]
      D[k]-=1
      L-=1
  D[s] = D.get(s,0)+1
  L+=1
maxL = max(L,maxL)
print(maxL)