N=int(input())
K=int(input())
S=sorted([*map(int,input().split())])
D=[0 for _ in range(N)]
for i in range(1,N):
  D[i]=S[i]-S[i-1]
D.sort()

if(K==1):
  print(sum(D))
else:
  print(sum(D[:-(K-1)]))