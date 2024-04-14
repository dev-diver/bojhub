N=int(input())
M=int(input())
S=[*input().strip()]

A=[]
flag = False
i=0
cnt=0
while(i<len(S)):
  if(not flag and S[i]=="I"):
    flag=True
    i+=1
    continue
  if(flag):
    if(i+1<len(S) and S[i]=="O" and S[i+1]=="I"):
      cnt+=1
      i+=2
      continue
    else:
      flag=False
      if(cnt>0):
        A.append(cnt)
      cnt=0
      continue
  i+=1
if cnt>0: 
  A.append(cnt)
s=0
for a in A:
  s+=max(0,a-N+1)
print(s)