N,M = map(int, input().split())
S=[]
for _ in range(N):
  P,L = map(int, input().split())
  *K, = map(int, input().split())
  K.sort(reverse=True)
  if(P>=L):
    s=K[L-1]
  else:
    s=1
  S.append(s)
S.sort()

s=0
i=0
for e in S:
  s+=e
  if(s>M):
    break
  i+=1
print(i)