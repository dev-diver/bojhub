N=int(input())
A=[]
def mapdata(x):
  return (int(x[0]),x[1])
A=[mapdata(input().strip().split()) for _ in range(N)]
A.sort(key=lambda x:x[0])
for a in A:
  print(*a)
