N,M = map(int,input().split())
def sumOne(N):
  k = len(bin(N))
  s = 0
  for n in range(1,k+1):
    a = 1<<n
    m = (N+1)//a
    r = (N+1)%a
    b = a>>1
    result = m*b + max(0,r-b)
    s+=result
  return s
print(sumOne(M)-sumOne(N-1))