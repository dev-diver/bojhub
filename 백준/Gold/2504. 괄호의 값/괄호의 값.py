S=[*input().strip()]
pair={")":"(","]":"["}
mult={")":2,"]":3}
stk = []
fail=False
for s in S:
  if fail: break
  if(s=="(" or s=="["):
    stk.append(s)
  elif(s==")" or s=="]"):
    m = 0
    while(stk):
      k = stk.pop()
      if isinstance(k, int): 
        m+=k
      elif(k==pair[s]):
        stk.append(m*mult[s] if m>0 else mult[s])
        break
      else:
        fail = True
        break
    else:
      fail = True
      break

m = 0
while(stk):
  k = stk.pop()
  if(isinstance(k, int)): 
    m+=k
  else:
    fail=True
    break
print(0 if fail else m)