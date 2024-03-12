import math
N=int(input())

def display(k):
  if k<=1:
    return [["*"]]

  pattern = []
  small = display(k//3)

  for l in small:
    pattern.append(l*3)
  for l in small:
    mid = l + [" "]*len(l) + l
    pattern.append(mid)
  for l in small:
    pattern.append(l*3)

  return pattern

result = display(N)

if(N!=1):
  print('\n'.join(map(lambda x: ''.join(x),result)))