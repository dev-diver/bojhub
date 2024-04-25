N=[*input().strip()]
loOp = '+-'
hiOp = '*/'
out = []
stk = []
for token in N:
  if token in loOp:
    while(stk and stk[-1] != '('):
      out.append(stk.pop())
    stk.append(token)
  elif token in hiOp:
    while(stk and stk[-1] in hiOp):
      out.append(stk.pop())
    stk.append(token)
  elif token=="(":
    stk.append(token)
  elif token==")":
    while(stk[-1]!='('):
      out.append(stk.pop())
    stk.pop()
  else:
    out.append(token)
while(stk):
  out.append(stk.pop())
print(*out,sep='')