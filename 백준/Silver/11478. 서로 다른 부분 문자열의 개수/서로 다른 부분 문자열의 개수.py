#조합
import sys
input = sys.stdin.readline
S = input().strip()
W = set()

l = len(S)
for s in range(l):
  for e in range(s,l):
    W.add(S[s:e+1])
print(len(W))