N, M = map(int, input().split())
C = list(map(int, input().split()))

def func(x):
  cnt = 1
  s = 0
  for c in C:
    if s + c <= x:
      s += c
    else:
      cnt += 1
      s = c
  return cnt <= M

lo = max(C)
hi = sum(C)+1

while lo < hi:
  mid = (lo+hi)//2
  if func(mid):
    hi = mid
  else:
    lo = mid+1

print(lo)