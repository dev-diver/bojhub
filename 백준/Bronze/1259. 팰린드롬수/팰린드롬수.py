ans=[]
while((w:=input().strip())!='0'):
  k=''.join(reversed(w))
  r = 'yes' if w==k else 'no'
  ans.append(r)
print(*ans,sep='\n')