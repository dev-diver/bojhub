N=int(input())
T=[tuple(map(int,input().split())) for _ in range(N)]
T.sort(key = lambda x : x[0])

leftMax = T[0] #(x,h)
leftS = 0
for x,h in T:
  if(h>leftMax[1]):
    leftS += (x-leftMax[0])*leftMax[1]
    leftMax = (x,h)

rightMax = T[-1]
rightS = 0
for x,h in reversed(T):
  if(h>rightMax[1]):
    rightS += (rightMax[0]-x)*rightMax[1]
    rightMax = (x,h)

maxS = (rightMax[0]-leftMax[0]+1)*leftMax[1]

print(leftS+maxS+rightS)