S=[*input().strip()]
stk = []
fail=False
for s in S:
  if(s=="("):
    stk.append("(")
  elif(s=="["):
    stk.append("[")
  elif(s==")"):
    m = 0
    while(len(stk)>0 and stk[-1]!="(" and stk[-1]!="["):
      m += stk.pop()
    if(len(stk)>0 and stk[-1]=="("):
      stk.pop()
      stk.append(m*2 if m>0 else 2)
    else:
      fail = True
      break
  elif(s=="]"):
    m = 0
    while(len(stk)>0 and stk[-1]!="(" and stk[-1]!="["):
      m += stk.pop()
    if(len(stk)>0 and stk[-1]=="["):
      stk.pop()
      stk.append(m*3 if m>0 else 3)
    else:
      fail=True
      break

m = 0
while(len(stk)>0 and stk[-1]!="(" and stk[-1]!="["):
  m += stk.pop()
if(len(stk)>0):
  fail=True
print(0 if fail else m)