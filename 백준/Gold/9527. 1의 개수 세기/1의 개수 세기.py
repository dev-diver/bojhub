N,M = map(int,input().split())
def getOrd(N):
  k=0
  a=1
  while(a<=N):
    k+=1
    a=a<<1
  return k

def sumOne(N):
  k = getOrd(N)
  s = 0
  for n in range(1,k+1):
    a = 1<<n
    m = (N+1)//a
    r = (N+1)%a
    c = m*(a>>1)
    d = max(0,r-(a>>1))
    result = c + d
    s+=result
  return s

print(sumOne(M)-sumOne(N-1))