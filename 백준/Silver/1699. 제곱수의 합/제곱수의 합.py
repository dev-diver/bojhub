N = int(input())
maxi = int(N**0.5)
S = {i*i for i in range(1,maxi+1)}
def div(N):
  for s in S:
    if((N-s) in S):
      return True
  return False

if N in S:
  print(1)
elif div(N):
  print(2)
else:
  while(N%4==0):
    N//=4
  if(N%8==7):
    print(4)
  else:
    print(3)