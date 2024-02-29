N = int(input())
C = [*map(int, input().split())]
M = int(input())
R = [*map(int,input().split())]
C.sort()

def bisect_left(arr,x):
  lo = 0
  hi = len(arr)
  while lo < hi:
    mid = (lo+hi)//2
    if arr[mid] < x:
      lo = mid+1
    else:
      hi = mid
  return hi
#not found return len(arr)

def bisect_right(arr, x):
  lo = 0
  hi = len(arr)
  while lo < hi:
    mid = (lo+hi)//2
    if arr[mid] <= x:
      lo = mid+1
    else:
      hi = mid
  return hi
#not found return -1

result = []
for r in R:
  left = bisect_left(C,r)
  if(left>=len(C) or r!=C[left]):
    result.append(0)
  else:
    right = bisect_right(C,r)
    result.append(right-left)

print(" ".join(map(str,result)))