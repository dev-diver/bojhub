#스위핑
N,M,L,K=map(int,input().split())
S = [tuple(map(int,input().split())) for _ in range(K)]
S.sort(key=lambda x:x[0])

def maxStarsOnLine(i):
  xhead = S[i][0]
  xtail = xhead + L
  k = i
  yStars = []
  while k<K and S[k][0] <= xtail:
    yStars.append(S[k][1])
    k+=1

  yStars.sort()
  mx = 0
  l = -1
  for yIndex in range(len(yStars)):
    y = yStars[yIndex]
    if(y==l): continue
    if(l!=-1 and l+L>=yStars[-1]) : break
    l=y
    k = yIndex
    s = 0
    while(k<len(yStars) and yStars[k]<=l+L):
      s+=1
      k+=1
    mx = max(mx,s)
  return mx

l = -1
mx = 0
for i in range(K):
  s = S[i]
  x,y = s
  if(x==l): continue
  if(l!=-1 and l+L>=S[-1][0]): break
  l=x
  mx = max(mx, maxStarsOnLine(i))
print(K-mx)
