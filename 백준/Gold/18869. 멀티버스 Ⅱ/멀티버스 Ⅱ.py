from itertools import combinations
M,N = map(int,input().split())
U = []
for _ in range(M):
  u = [(v,i) for i,v in enumerate([*map(int,input().split())])]
  u.sort()
  o = [0]*N
  o[u[0][1]] = 0
  k=0
  for i in range(1,N):
    if(u[i][0]!=u[i-1][0]): k+=1
    o[u[i][1]] = k
  U.append(o)

result = 0
for a,b in combinations(U,2):
  flag = True
  for i in range(N):
    if(a[i]!=b[i]):
      flag = False
      break
  if not flag: continue
  result+=1
print(result)
