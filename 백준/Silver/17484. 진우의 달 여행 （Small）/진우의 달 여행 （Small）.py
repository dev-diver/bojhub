N,M = map(int, input().split())
F = [[*map(int, input().split())] for _ in range(N)]
directions = [-1,0,1]

def simulate(curr,fuel, curDir): #(x,y)
  x,y = curr
  if(x==N-1):
    return fuel
  m = float('inf')
  for dir in directions:
    nextX, nextY = x+1, y+dir
    if(dir!=curDir and 0<=nextY<M):
      m = min(m, simulate((nextX,nextY),fuel+F[nextX][nextY],dir))
  return m

m=float('inf')
for i in range(M):
  m = min(m, simulate((0,i), F[0][i], -2))
print(m)