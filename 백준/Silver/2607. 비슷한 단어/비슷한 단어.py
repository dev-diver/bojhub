import sys
input = sys.stdin.readline
N=int(input())
S=input().rstrip()
W=[]
for _ in range(N-1):
   W.append(input().rstrip())

def changeToDict(S):
    d = dict()
    for s in S:
        d[s] = d.get(s,0) + 1
    return d

def isSim(S,W):
    s = changeToDict(S)
    w = changeToDict(W)

    for ch in w:
        s[ch] = s.get(ch,0)-w[ch]
    diff = 0
    total=0
    for ch in s:
        diff += abs(s[ch])
        total += s[ch]
    return True if (abs(total)<=1 and diff<=2) or diff<=1 else False

s=0
for w in W:
    s+= 1 if isSim(S,w) else 0

print(s)
