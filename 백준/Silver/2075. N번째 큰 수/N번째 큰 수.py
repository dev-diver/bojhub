import sys
import heapq
input = sys.stdin.readline
N = int(input())
Q=[]
for _ in range(N):
  *temp, = map(lambda x:-int(x),input().split())
  temp = temp+Q
  Q=[]
  heapq.heapify(temp)
  for _ in range(N):
    n = -heapq.heappop(temp)
    Q.append(-n)
print(-Q[-1])