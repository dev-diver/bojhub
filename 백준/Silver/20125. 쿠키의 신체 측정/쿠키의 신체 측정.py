N=int(input())

def findStar(S):

  i = S.find("*")
  if(i==-1):
    return (-1,0)
  cnt=1
  for j in range(i+1,len(S)):
    if(S[j]=="_"):
      break
    cnt+=1
  return (i+1,cnt)

heart = (0,0)
arm = [0,0] #left, right
back = 0
leg = [0,0] #left, right
for row in range(1,N+1):
  S = input()
  i, cnt = findStar(S)
  if(i==-1): continue
  elif(heart[0]==0):
    heart = (row+1,i)
  elif(arm[0]==0):
    arm[0] = heart[1]-i
    arm[1] = cnt - arm[0] -1
  elif(i==heart[1]):
    back+=1
  else:
    if(S[heart[1]-2]=="*"):
      leg[0]+=1
    if(S[heart[1]]=="*"):
      leg[1]+=1
    
print(*heart)
print(*arm, back, *leg)