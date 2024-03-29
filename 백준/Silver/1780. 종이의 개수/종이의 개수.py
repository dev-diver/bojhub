import sys
input = sys.stdin.readline
N = int(input())
MAP = [[*map(int, input().split(' '))] for _ in range(N)]

def allSame(M):
  e = M[0][0]
  for line in M:
    for elem in line:
      if elem!=e: return False
  return True

def countElem(elem):
  if elem ==-1:
    cnt[0]+=1
  elif elem == 0:
    cnt[1]+=1
  elif elem == 1:
    cnt[2]+=1

def dfs(M,K):
  if(K==1 or allSame(M)):
    countElem(M[0][0])
    return
  section = [(0,K//3),(K//3,K//3*2),(K//3*2,K)]
  for xs,xe in section:
    for ys,ye in section:
      m = [line[ys:ye] for line in M[xs:xe]]
      dfs(m,K//3)

global cnt
cnt = [0,0,0]
dfs(MAP,N)

print('\n'.join([*map(str,cnt)]))