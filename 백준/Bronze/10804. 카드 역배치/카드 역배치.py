import sys
input = sys.stdin.readline
R = [[*map(int, input().split())] for _ in range(10)]
arr = [str(i) for i in range(0,21)]
for rs,re in R:
  arrc = arr[rs:re+1]
  for i in range(rs,re+1):
    j = i-rs
    arr[i] = arrc[-j-1]
print(' '.join(arr[1:]))