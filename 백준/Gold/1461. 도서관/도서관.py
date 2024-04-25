N,K = map(int, input().split())
*S, = map(int,input().split())
S.sort()
neg = []
pos = []
walk=0
for s in S:
  if(s>0):
    pos.append(s)
  else:
    neg.append(s)
neg.reverse()
posq = len(pos)//K
negq = len(neg)//K
posr = len(pos)%K
negr = len(neg)%K
for i in range(posq + (posr!=0)):
  walk+=pos[posr-1+i*K]*2
for i in range(negq + (negr!=0)):
  walk-=neg[negr-1+i*K]*2
negm = -neg[-1] if neg else 0
posm = pos[-1] if pos else 0
walk-=max(negm,posm)
print(walk)