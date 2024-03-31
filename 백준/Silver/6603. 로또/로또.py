#순열  #permutation
import sys
input = sys.stdin.readline

def comb(n, arr, path):
  if(n==0):
    print(*path)
    return

  for i in range(len(arr)-n+1):
    path.append(arr[i])
    comb(n-1, arr[i+1:], path)
    path.pop() 

while True:
  k,*arr = [*map(int, input().split())]
  if(k==0): break
  paths = []
  comb(6,arr,[])
  print()
  
  
