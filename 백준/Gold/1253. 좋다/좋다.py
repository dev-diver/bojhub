import sys
input = sys.stdin.readline
N=int(input())
*S,=map(int,input().split())
S.sort()
result=0
for i in range(N):
  target = S[i]
  left,right = 0,N-1
  while(left<right):
    total = S[left]+S[right]
    if(target==S[left]+S[right]):
      if(left==i):
        left+=1
      elif(right==i):
        right-=1
      else:
        result+=1
        break
    elif(target<total):
      right-=1
    else:
      left+=1

print(result)
