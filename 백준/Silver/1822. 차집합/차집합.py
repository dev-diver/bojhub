import sys
input = sys.stdin.readline
N,M = input().split(' ')
A = set([*map(int,input().split(' '))])
B = set([*map(int,input().split(' '))])
C = sorted(A-B)
print(len(C))
if(len(C)>0):
  result = [*map(str, C)]
  print(' '.join(result))