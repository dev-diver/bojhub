import sys,os,io
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
N,L = map(int,input().split())
M = []
for _ in range(N):
  s,e = map(int,input().split())
  M.append((s,e))
M.sort()

E = 0
cnt = 0
for s,e in M:
  start = max(s,E)
  l = (e-start)//L
  cnt+=l
  E = start + l*L
  if(E<e):
    cnt+=1
    E += L
sys.stdout.write(str(cnt))