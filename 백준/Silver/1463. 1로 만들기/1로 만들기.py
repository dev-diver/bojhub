N=int(input())
Mem=[0,0]

for i in range(2,N+1):
  Div3, Div2, Sub1 = [N]*3
  if(i%2==0): Div2= Mem[i//2]
  if(i%3==0): Div3= Mem[i//3]
  Sub1 = Mem[i-1]
  Mem += [min(Div2, Div3, Sub1) + 1]

print(Mem[-1])
