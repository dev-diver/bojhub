import sys
input = sys.stdin.readline
N,M = input().split(' ')
Ai = [*map(int,input().split(' '))]
Bi = [*map(int,input().split(' '))]
A = set()
B = set()
for a in Ai:
  A.add(a)
for b in Bi:
  B.add(b)
C = A-B
sC = sorted(C)
print(len(C))
if(len(C)>0):
  result = [*map(str, sC)]
  print(' '.join(result))