ans=[]
while((w:=sorted(map(lambda x:int(x)**2,input().split())))[0]):
  ans.append('right' if w[0]+w[1]==w[2] else 'wrong')
print(*ans,sep="\n")