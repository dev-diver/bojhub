import sys
input = sys.stdin.readline
T = int(input())

def make(path):
  paths = []
  for p in path:
    ap = abs(p)
    t='+'+str(p) if p>0 else str(p)
    if(ap>=10):
      paths.append(t[:2])
      for s in t[2:]:
        paths.append(' '+s)
    else:
      paths.append(t)
  return ''.join(paths)[1:] 
    
def dfs(N):
  paths = []
  stk = [[1,[1],2]]
  while stk:
    s,path,next_num = stk.pop()
    if(next_num==N+1):
      if(s==0):
        paths.append(make(path))
      continue
    stk.append([s+next_num,path+[next_num],next_num+1])
    stk.append([s-next_num,path+[-next_num],next_num+1])
    k = path[-1]
    s -= k
    x = k*10+next_num if k>0 else k*10-next_num
    stk.append([s+x,path[:-1]+[x],next_num+1])
  return paths

for i in range(T):
  N = int(input())
  paths = dfs(N)
  paths.sort()
  print(*paths,sep="\n")
  print()