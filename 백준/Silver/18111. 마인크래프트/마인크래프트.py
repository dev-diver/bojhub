N,M,B=map(int,input().split())
T = [[*map(int,input().split())] for _ in range(N)]

def calCost(H,T,B):
  dig=0
  stack=0
  for i in range(N):
    for j in range(M):
      h=T[i][j]
      if(H<h):
        dig+=(h-H)
      else:
        stack+=(H-h)
  if(B>=stack-dig):
    return dig*2+stack
  else:
    return float('inf')

Cost = dict()
minB = min([min(line) for line in T])
maxB = max([max(line) for line in T])
for H in range(minB,maxB+1):
  cost = calCost(H,T,B)
  Cost[H] = cost
R = sorted(Cost, key=lambda x:(Cost[x],-x))[0]
print(Cost[R],R)