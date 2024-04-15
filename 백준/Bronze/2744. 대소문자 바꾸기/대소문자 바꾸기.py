diff = ord('a')-ord('A')
def chg(x):
  o = ord(x)
  if 'a'<=x<='z':
    return chr(o-diff)
  else:
    return chr(o+diff)
S=[*map(chg, input().strip())]
print(''.join(S))