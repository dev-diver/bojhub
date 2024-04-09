M=int(input())
batchSize = int(1e3)
batch = M//batchSize
remain = M%batchSize

S=0
# print(bin(S)[2:].zfill(20))
def process(ans):
  global S
  cmd,*x = input().strip().split()
  if(cmd=='all'):
    S=(1<<20)-1
  elif(cmd=='empty'):
    S=0
  else:
    x=int(x[0])-1
    if(cmd=='add'):
      S|=(1<<x)
    elif(cmd=='remove'):
      S&=~(1<<x)
    elif(cmd=='check'):
      ans.append((S>>x)&1)
    elif(cmd=='toggle'):
      S^=(1<<x)

for _ in range(batch):
  ans=[]
  for _ in range(batchSize):
    process(ans)
  if(ans): print(*ans, sep="\n")

ans=[]
for _ in range(remain):
  process(ans)
print(*ans, sep="\n")    
  
  