import sys
import heapq
input = sys.stdin.readline
N=int(input())
P = [[] for _ in range(N)]
outdeg = [0]*N
for i in range(N):
  *l, = map(int,[*input().strip()])
  for j in range(N):
    if(l[j]==1):
      P[j].append(i)
      outdeg[i]+=1
Q=[]
for i in range(N):
  if(outdeg[i]==0):
    heapq.heappush(Q,-i)

ans=[]
while Q:
  n = -heapq.heappop(Q)
  ans.append(n)
  for p in P[n]:
    if(outdeg[p]>0):
      outdeg[p]-=1
      if(outdeg[p]==0):
        heapq.heappush(Q,-p)

O=[0]*N
if(len(ans)!=N):
  print(-1)
else:
  for i in range(N):
    O[ans[i]]=N-i
  print(*O)