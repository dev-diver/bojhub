ans=[]
while((w:=input().strip())!='0'):
  flag='yes'
  L=len(w)//2
  for i in range(L) :
      if w[i] != w[-1- i] :
          flag = "no"
          break
  ans.append(flag)
print(*ans,sep='\n')