N=int(input())
*S,= map(int,input().split())
S.sort()
result = int(1e7)
for i in range(N):
  result = min(result,S[i]+S[-i-1])
print(result)