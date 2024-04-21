import sys
input = sys.stdin.readline
N,K = map(int,input().split())
M = [[*map(int, input().split())] for _ in range(N)]
M.sort(key=lambda x:(-x[1],-x[2],-x[3]))
for i in range(N):
  if(M[i][0]==K):
    k=1
    while(M[i][1:]==M[i-k][1:]):
      k+=1
    print(i-k+2)