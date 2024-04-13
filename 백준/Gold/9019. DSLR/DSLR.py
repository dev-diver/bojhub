from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

def applyCmd(cmd, n:int):
  if(cmd=="D"):
    n = 2*n%10000
  elif(cmd=="S"):
    n = n-1
    if(n==-1) : n=9999
  else:
    d4 = n % 10
    d3 = n//10 % 10
    d2 = n//100 % 10
    d1 = n//1000 % 10
    if(cmd=="L"):
      d1,d2,d3,d4 = d2, d3, d4, d1
    elif(cmd=="R"):
      d1,d2,d3,d4 = d4, d1, d2, d3
    n = d1*1000 + d2*100 + d3*10 + d4
  return n

for _ in range(T):
  S,E = map(int, input().split())
  V = [""]*10000
  Q = deque([S])
  V[S] = " "
  path = ""
  operations = ["D","S","L","R"]
  while Q:
    num = Q.popleft()
    if(num==E):
      path = V[num]
      break
    for operate in operations:
      nextNum = applyCmd(operate, num)
      if(V[nextNum]==""):
        V[nextNum] = V[num]+operate
        Q.append(nextNum)
  print(path.lstrip())
