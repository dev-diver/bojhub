N,M = map(int,input().split())
S=dict()
K=['']*(N+1)
for i in range(1,N+1):
  name = input().strip()
  S[name] = i
  K[i]=name
for i in range(M):
  cmd = input().strip()
  if(cmd.isnumeric()):
    print(K[int(cmd)])
  else:
    print(S[cmd])