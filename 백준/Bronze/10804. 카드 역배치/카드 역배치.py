import sys
input = sys.stdin.readline
arr = [i for i in range(0,21)]
for _ in range(10):
  s, e = map(int, input().split(' '))
  arr[s:e+1] = arr[s:e+1][::-1]
print(*arr[1:])