N,M,B=map(int,input().split())
T = [[*map(int,input().split())] for _ in range(N)]
Cost = dict()

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

for H in range(257):
  cost = calCost(H,T,B)
  Cost[H] = cost
R = sorted(Cost, key=lambda x:(Cost[x],-x))[0]
print(Cost[R],R)