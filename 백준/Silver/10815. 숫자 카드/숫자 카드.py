N = int(input())
C = [*map(int, input().split())]
M = int(input())
Check = [*map(int,input().split())]
C.sort()

def find(x):
  lo = 0
  hi = len(C)-1
  while lo < hi:
    mid = (lo+hi)//2
    if(C[mid]<x):
      lo = mid+1
    else:
      hi = mid
  if(C[hi]!=x):
    return 0
  else:
    return 1

ans = []
for c in Check:
  ans.append(find(c))

print(" ".join(map(str,ans)))