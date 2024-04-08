N=int(input())
P=[(*map(int,input().split()),) for _ in range(N)]
P.sort(key=lambda x:x)
for p in P:
  print(*p)