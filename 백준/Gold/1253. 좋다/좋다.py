N=int(input())
*S,=map(int,input().split())
S.sort()
result=0
for i in range(N):
  temp = S[:i]+S[i+1:]
  start,end = 0,len(temp)-1
  while(start<end):
    total = temp[start]+temp[end]
    if(S[i]==total):
      result+=1
      break
    elif(S[i]<total):
      end-=1
    else:
      start+=1
      
print(result)