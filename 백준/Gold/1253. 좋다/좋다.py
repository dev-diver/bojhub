N=int(input())
*S,=map(int,input().split())
S.sort()
result=0
for i in range(N):
  for j in range(N):
    if(j==i): continue
    lo = j+1
    hi = N
    while(lo<hi):
      mid = (lo+hi)//2
      if(S[i]>S[j]+S[mid]): #True
        lo = mid +1
      else:
        hi = mid
    k = lo
    while(k==i or k==j):
      k+=1
    if(k<N and S[i]==S[j]+S[k]):
      result += 1
      break

print(result)
