import sys
input = sys.stdin.readline
N = int(input())
stk = [0]
for _ in range(N):
  K = int(input())
  while(stk and stk[-1]<=K):
    stk.pop()
  stk.append(K)

print(len(stk))
