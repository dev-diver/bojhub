import sys
N=int(sys.stdin.readline())
Stairs=[int(sys.stdin.readline().strip()) for _ in range(N)]

mem=[[-1,-1] for _ in range(N)]

def Climb(stair, one):

  if(stair >= len(Stairs)) : return 0
  
  if(mem[stair][one]!= -1): return mem[stair][one]
  
  if(stair==N-2 and one==1): return 0
  if (one == 0): sum = max(Climb(stair+1, one+1), Climb(stair+2, 0))
  if (one == 1): sum = Climb(stair+2, 0)  
  if (one >= 2) : return 0
  
  sum+= Stairs[stair]
  mem[stair][one] = sum
  
  return sum
  
print(max(Climb(0,0), Climb(1,0)))