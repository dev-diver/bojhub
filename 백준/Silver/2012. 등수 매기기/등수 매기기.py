N=int(input())
S=[int(input()) for _ in range(N)]
S.sort()
s = 0
for i in range(N):
  s += abs(S[i]-(i+1))
print(s)