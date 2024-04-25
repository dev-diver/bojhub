import sys
sys.setrecursionlimit(10000)
S1= list(sys.stdin.readline().strip())
S2= list(sys.stdin.readline().strip())
same = [[0]*len(S2) for _ in range(len(S1))]
mem  = [[-1]*len(S2) for _ in range(len(S1))]

for i in range(len(S1)):
  for j in range(len(S2)):
    if(S1[i]==S2[j]): same[i][j] = 1

def FindLCS(i,j):
  
  if(i>=len(S1) or j>=len(S2)): return 0
  if(mem[i][j]!= -1): return mem[i][j]
  
  if(same[i][j]==1): result = FindLCS(i+1,j+1) + 1
  else: result = max(FindLCS(i+1,j), FindLCS(i,j+1))
  mem[i][j] = result
  return result

L=FindLCS(0,0)
print(L)

Str=""
for i in range(len(S1)):
  for j in range(len(S2)):
    if(mem[i][j]==L and same[i][j]==1): 
      Str+=S1[i]
      L-=1
      break;
print(Str)