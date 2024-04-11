N=int(input())
M=int(input())
*dNum, = input().strip().split() if M!=0 else []
*nums, = filter(lambda x: x not in dNum,[str(i) for i in range(10)])

def dfs(num, depth):
  if(len(num)==depth):
    return len(str(int(num)))+abs(int(num)-N)

  m = float('inf')
  for nextClick in nums:
    m = min(m, dfs(num+str(nextClick), depth))
  return m

size = len(str(N))
m = abs(100-N)
for depth in range(max(1,size-1),size+2):
  for firstClick in nums:
      m = min(m, dfs(firstClick, depth))
print(m)