import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
N,K = map(int,input().split())
*S, = map(int,input().split())
D = [0]*100_001
L = 0
maxL = 0
for i in range(N):
  s = S[i]
  while(D[s]+1>K):
    k = S[i-L]
    D[k]-=1
    L-=1
  D[s] += 1
  L+=1
  maxL = max(L,maxL)
sys.stdout.write(str(maxL))