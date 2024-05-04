N,K = map(int,input().split())
*S, = map(int,input().split())
head = 0
tail = 0
odd = 0
while(tail<N and odd<K):
  if(S[tail]%2==1):
    odd+=1
  tail+=1
result = tail-head-odd
while(tail<=N):
  while(head<N and S[head]%2==0):
    head+=1
  head+=1
  while(tail<N and S[tail]%2==0):
    tail+=1
  tail+=1
  while(tail<N and S[tail]%2==0):
    tail+=1
  temp = tail-head-odd
  result = max(result, temp)
print(result)
