N=int(input())

def biggestN(N,i):
  return N//(10**i)

A = [[] for _ in range(10)]
A[0] = [i for i in range(10)]
s=10
find=-1
for i in range(1,10):
  for j in range(1,10):
    for k in A[i-1]:
      K = biggestN(k,i-1)
      if(K<j):
        val = j*(10**i)+k
        A[i].append(val)
        s+=1
        if(s>N):
          find = val
          break
      else:
        break
      if find!=-1:break
    if find!=-1:break
  if find!=-1:break

if N<=10:
  print(N)
elif not find:
  print(-1)
else:
  print(find)