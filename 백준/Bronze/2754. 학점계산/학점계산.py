G=[*input().strip()]
if(G[0]=='F'):
  print(0.0)
else:
  B='DCBA'.index(G[0])+1
  P=('-0+'.index(G[1])-1)*0.3
  print(B+P)