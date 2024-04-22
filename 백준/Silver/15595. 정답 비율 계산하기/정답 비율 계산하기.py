T = int(input())
correct={}
wrong={}
for _ in range(T):
  n,user,case,_,_,_,_ = input().strip().split()
  if(user=='megalusion'):
    continue
  if(case=='4'):
    correct[user] = wrong.get(user,0)
  elif(user not in correct):
    wrong[user] = wrong.get(user,0)+1
wrongcnt = 0
for i in correct:
  wrongcnt+=correct[i]
ans = len(correct)/(len(correct)+wrongcnt)*100 if len(correct)>0 else 0
print(ans)