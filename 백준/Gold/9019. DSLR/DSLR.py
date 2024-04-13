from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

def applyCmd(cmd, n:int):
  if(cmd=="D"):
    n = n<<1
  elif(cmd=="S"):
    n = n-1
  elif(cmd=="L"):
    n = n*10+(n//1000)%10
  elif(cmd=="R"):
    n = n%10*1000 + n//10
  return n%10000

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
