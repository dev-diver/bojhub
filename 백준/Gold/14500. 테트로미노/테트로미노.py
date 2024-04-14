import sys
input = sys.stdin.readline
N,M = map(int,input().split())
T = [[*map(int,input().split())] for _ in range(N)]

m = 0
#1*4
def s1_4(x,y):
  s=0
  for i in range(4):
    s+=T[x][y+i]
  return s

for i in range(N):
  for j in range(M-3):
    m = max(m,s1_4(i,j))

#4*1
def s4_1(x,y):
  s=0
  for i in range(4):
      s+=T[x+i][y]
  return s

for i in range(N-3):
  for j in range(M):
    m = max(m,s4_1(i,j))

#2*2
def s2_2(x,y):
  s=0
  for i in range(2):
    for j in range(2):
      s+=T[x+i][y+j]
  return s

for i in range(N-1):
  for j in range(M-1):
    m = max(m,s2_2(i,j))

#2*3  8개
blocks = [(1,0,0,1,1,1),(1,1,1,0,0,1),(1,1,1,1,0,0),(0,0,1,1,1,1),
          (0,1,1,1,1,0),(1,1,0,0,1,1),(0,1,0,1,1,1),(1,1,1,0,1,0)]
def s2_3(x,y):
  m=0
  for block in blocks:
    s=0
    for i in range(2):
      for j in range(3):
        if(block[i*3+j]==1):
          s+=T[x+i][y+j]
    m=max(m,s)
  return m

for i in range(N-1):
  for j in range(M-2):
    m = max(m,s2_3(i,j))

#3*2
def s3_2(x,y):
  m=0
  for block in blocks:
    s=0
    for i in range(3):
      for j in range(2):
        if(block[j*3+i]==1):
          s+=T[x+i][y+j]
    m=max(m,s)
  return m

for i in range(N-2):
  for j in range(M-1):
    m = max(m,s3_2(i,j))

print(m)