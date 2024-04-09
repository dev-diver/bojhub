N=int(input())
def roundUp(x):
    if (x - int(x)) >= 0.5:
        return int(x)+1
    else:
        return int(x)

if(N==0): print(0)
else:
  S = [int(input()) for _ in range(N)]
  S.sort()
  d = roundUp(N*0.15)

  s = sum(S[d:-d]) if d !=0 else sum(S)
  print(roundUp(s/(N-2*d)))