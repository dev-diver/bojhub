import sys
input=sys.stdin.readline
M=int(input())
S=0
for _ in range(M):
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
      sys.stdout.write(str((S>>x)&1)+'\n')
    elif(cmd=='toggle'):
      S^=(1<<x)