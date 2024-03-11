n=int(input())
table = [0,1,2]
for i in range(3,n+1):
  r = table[i-1] + table[i-2]
  table.append(r%10007)
print(table[n])