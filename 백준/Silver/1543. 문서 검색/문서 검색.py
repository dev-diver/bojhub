#그리디
import sys
input = sys.stdin.readline
D = input().strip()
W = input().strip()

i = 0
cnt = 0
while(i<len(D)-len(W)+1):
  if(D[i]==W[0]):
    j=0
    while(j<len(W) and D[i+j]==W[j]):
      j+=1
    if(j==len(W)):
      i=i+j-1
      cnt+=1
  i+=1
print(cnt)
    
  
