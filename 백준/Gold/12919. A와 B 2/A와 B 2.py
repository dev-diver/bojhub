S=input().rstrip()
T=input().rstrip()
stk = [T]
find = False

while(stk):
  t = stk.pop()
  if(len(t)<=len(S)):
    if(t!=S):
      continue
    else:
      find = True
      break
  if(t[-1]=='A'):
    stk.append(t[:-1])
  if(t[0]=='B'):
    stk.append(t[-1:0:-1])
print(1 if find else 0)
