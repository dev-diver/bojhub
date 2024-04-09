N=int(input())
F=[1]*(N+1)
C=[0]*(N+1)

def div(n):
  cnt=0
  while(n%10==0):
    n//=10
    cnt+=1
  return (n,cnt)

for i in range(1,N+1):
  f=F[i-1]*i
  f,n=div(f)
  F[i]=f  
  C[i]=C[i-1]+n
print(C[-1])