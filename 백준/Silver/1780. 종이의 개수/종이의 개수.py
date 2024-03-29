import sys
input = sys.stdin.readline
N = int(input())
M = [[*map(int, input().split(' '))] for _ in range(N)]

def allSame(x,y,k):
  e = M[x][y]
  for i in range(x,x+k):
    for j in range(y,y+k):
      if M[i][j] != e: return False
  return True

def countElem(elem):
  cnt[elem+1]+=1

def dfs(x,y,k):
  if(k==1 or allSame(x,y,k)):
    countElem(M[x][y])
    return
  nk = k//3
  section = [0,nk,nk*2]
  for nx in section:
    for ny in section:
      dfs(x+nx,y+ny,nk)

global cnt
cnt = [0,0,0]
dfs(0,0,N)

print('\n'.join([*map(str,cnt)]))