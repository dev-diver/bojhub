N = int(input())
S=set()
for _ in range(N):
  name, state = input().strip().split()
  if(state=="enter"):
    S.add(name)
  elif(state=="leave"):
    S.remove(name)
A=sorted(S)
A.reverse()
print(*A, sep="\n")