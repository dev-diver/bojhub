a= int(input())
b= int(input())
c= int(input())
res = list(str(a*b*c))
ans = [0 for x in range(10)]
for x in res:
  ans[int(x)]+=1
print('\n'.join(map(str,ans)))