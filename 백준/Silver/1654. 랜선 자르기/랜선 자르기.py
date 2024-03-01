K,N = map(int,input().split())
L = [int(input()) for _ in range(K)]

def func(x):
  s=0
  for l in L:
    s += l//x
  return s>=N

lo = 1
hi = max(L)+1
while lo < hi:
  mid = (lo+hi)//2
  if func(mid):
    lo = mid+1
  else:
    hi = mid

print(hi-1)