#누적합, 시뮬레이션?
U = [*map(int,input().split())]
S = [*map(int,input().split())]

u = 0
s = 0
ans='No'
for i in range(9):
  u += U[i]
  if(u>s):
    ans='Yes'
    break
  s += S[i]
print(ans)