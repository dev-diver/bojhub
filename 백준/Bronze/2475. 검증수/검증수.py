*N, = map(int, input().split())
s=0
for n in N:
  s+=n*n
print(s%10)