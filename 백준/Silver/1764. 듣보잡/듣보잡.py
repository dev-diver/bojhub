N,M=map(int,input().split())
H = set()
S = set()
for _ in range(N):
  name = input().strip()
  H.add(name)
for _ in range(M):
  name = input().strip()
  if(name in H):
    S.add(name)
print(len(S))
print(*sorted(S),sep="\n")
