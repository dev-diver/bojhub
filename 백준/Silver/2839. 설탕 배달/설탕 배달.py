i=int(input());c=0
while i%5:i-=3;c+=1
print(-1 if i<0 else i//5+c)