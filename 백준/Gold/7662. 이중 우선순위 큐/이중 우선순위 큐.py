import sys
import heapq
input = sys.stdin.readline
T = int(input())
ans=[]
for _ in range(T):
  k = int(input())
  lQ = []
  hQ = []
  deleted = [False]*k
  for i in range(k):
    cmd, num = input().strip().split()
    num = int(num)
    if(cmd == "I"):
      heapq.heappush(lQ, (num, i)) #최소힙
      heapq.heappush(hQ, (-num,i)) #최대힙
    if(cmd == "D"):
      if(num == 1):
        while hQ and deleted[hQ[0][1]]:
          heapq.heappop(hQ)
        if hQ:
          n, i = heapq.heappop(hQ)
          deleted[i] = True
      elif(num == -1):
        while lQ and deleted[lQ[0][1]]:
          heapq.heappop(lQ)
        if lQ:
          n, i = heapq.heappop(lQ)
          deleted[i] = True
  while lQ and deleted[lQ[0][1]]:
    heapq.heappop(lQ)
  while hQ and deleted[hQ[0][1]]:
    heapq.heappop(hQ)
  if(not lQ):
    ans.append("EMPTY")
  else:
    h = -hQ[0][0]
    l = lQ[0][0]
    ans.append(str(h) + " " + str(l))
  # print(lQ, hQ, deleted)
print(*ans,sep="\n")