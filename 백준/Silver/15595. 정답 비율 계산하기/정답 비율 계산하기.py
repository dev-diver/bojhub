import sys,io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
T = int(input())
correct={}
wrong={}
cnt=0
for _ in range(T):
  _,user,case,_,_,_,_ = input().strip().split()
  if(user==b'megalusion' or user in correct):
    continue
  if(case==b'4'):
    wr = wrong.get(user,0)
    cnt += wr
    correct[user] = wr
  else:
    wrong[user] = wrong.get(user,0)+1
ans = len(correct)/(len(correct)+cnt)*100 if len(correct)>0 else 0
sys.stdout.write(str(ans))