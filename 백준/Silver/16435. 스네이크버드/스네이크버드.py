#시뮬레이션
import sys
input = sys.stdin.readline
N,L = map(int, input().split())
A = [*map(int, input().split())]
A.sort()

for a in A:
  if(a<=L):
    L+=1
print(L)