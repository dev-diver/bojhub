import itertools
import sys
from itertools import combinations
input = sys.stdin.readline

def calDist(A,B):
  dist = 0
  for i in range(len(A)):
    if(A[i]!=B[i]):
      dist+=1
  return dist

def calThree(A,B,C):
  s = 0
  Comb = combinations([A,B,C],2)
  for c in Comb:
    s+=calDist(*c)
  return s


T = int(input())
for _ in range(T):
  N = int(input())
  P = input().strip().split()
  S = dict()
  for p in P:
    if p in S:
      S[p]+=1
    else:
      S[p]=1
  if(max(S.values())>=3):
    print(0)
    continue
  K=[]
  for s in S:
    K.append(s)
    if(S[s]!=1):
      K.append(s)
  Comb = combinations(K,3)
  m = 12
  for c in Comb:
    m = min(m,calThree(*c))
  print(m)