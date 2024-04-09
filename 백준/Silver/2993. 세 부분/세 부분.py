T = input().strip()
L = len(T)
m='z'*L
for i in range(0,L-1):
  for j in range(i+1,L-1):
    pre=T[i::-1]
    mid=T[j:i:-1]
    post=T[:j:-1]
    s=pre+mid+post
    m=min(m,s)
print(m)