from collections import deque
N,L,W = map(int,input().split())
A = deque([*map(int,input().split())])

t=0
Q=deque([])
totalWeight = 0
while A:
  t+=1
  if(Q and t>=Q[0][1]+L):
    pop_truck = Q.popleft()
    totalWeight -= pop_truck[0]
  next_truck = A[0]
  if(totalWeight+next_truck<=W):
    next_truck = A.popleft()
    Q.append((next_truck,t))
    totalWeight += next_truck
print(t+L)