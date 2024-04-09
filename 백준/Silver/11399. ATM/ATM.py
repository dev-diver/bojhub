N=int(input())
*P,=map(int,input().split())
P.sort()
s=[P[0]]*N
for i in range(1,N):
  s[i]=s[i-1]+P[i]
for i in range(1,N):
  s[i]=s[i-1]+s[i]
print(s[-1])