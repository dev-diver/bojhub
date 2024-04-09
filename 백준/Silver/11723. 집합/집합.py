import sys
input=sys.stdin.readline
M=int(input())
S=0
for _ in range(M):
  c = input().split()
  if(c[0]=='all'):
    S=(1<<21)-1
  elif(c[0]=='empty'):
    S=0
  elif(c[0]=='add'):
    S|=(1<<(int(c[1])))
  elif(c[0]=='remove'):
    S&=~(1<<int(c[1]))
  elif(c[0]=='check'):
    sys.stdout.write("1\n" if S & (1 << int(c[1])) else "0\n")
  elif(c[0]=='toggle'):
    S^=(1<<int(c[1]))