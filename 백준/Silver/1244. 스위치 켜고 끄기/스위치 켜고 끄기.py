N = int(input())
*S, = map(int,input().split())
M = int(input())
def toggle(k):
  S[k] = 0 if S[k]==1 else 1
for _ in range(M):
  s,n = map(int,input().split())
  if(s==1):
    k=n
    while(k<=N):
      toggle(k-1)
      k+=n
  else:
    toggle(n-1)
    left = n-1
    right = n+1
    while(right<=N and left-1>=0 and S[left-1]==S[right-1]):
      toggle(left-1)
      toggle(right-1)
      left-=1
      right+=1

L=20
for i in range(0,N,L):
  print(*S[i:i+L])
