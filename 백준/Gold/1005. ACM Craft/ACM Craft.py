import sys
read = sys.stdin.readline
sys.setrecursionlimit(100000)

def minTime(B):
  
  if(mem[B]!=-1): return mem[B]
  maxT = 0
  for FirstB in Ord[B]:
    temp = minTime(FirstB)
    if(temp > maxT): maxT=temp
  
  mem[B] = maxT + D[B]
  return mem[B]
 
T=int(read())
for _ in range(T):
  N,K = map(int, read().split())
  D = [0] + list(map(int, read().split()))
  Ord = [[] for x in range(N+1)]
  for i in range(K):
    N1, N2 = map(int, read().split())
    Ord[N2] += [N1]
  W=int(read())
  
  mem=[-1]*(N+1)

  print(minTime(W))
