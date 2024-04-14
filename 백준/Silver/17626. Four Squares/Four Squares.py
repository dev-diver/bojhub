from collections import deque
N = int(input())
S = []
i=1
while True:
  s = i*i
  if(s<=N):
    S.append(s)
  else:
    break
  i+=1

Q = deque([(0,0)])
V = set()
while Q:
  n,d = Q.popleft()
  if(n==N):
    print(d)
    break
  for square in S:
    next_num = n+square
    if(next_num<=N and next_num not in V):
      Q.append((next_num,d+1))
      V.add(next_num)
