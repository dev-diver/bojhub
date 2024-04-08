#그리디 - 활동 선택 문제
#앞 사람이 되도록 앞쪽 햄버거를 먹어야 함
#정당성 증명: 
#(가정) 앞쪽 햄버거를 먹는 것이 최선(최적해)가 아니다.
#(최적해 가정)첫번째 사람이 가장 앞쪽 햄버거를 먹지 않은 경우가 최적해인 경우
#(모순)첫번째 사람이 가장 그보다 앞에 햄버거를 먹은 경우도 최적해가 나온다.
#따라서, 가장 앞쪽 햄버거를 먹는 것이 최적이 아니라는 데 모순된다.
N,K = map(int, input().split())
*R, = input().strip()
P = []
H = [0]*N
for i in range(N):
  if(R[i]=='P'):
    P.append(i)
  else:
    H[i]=1

cnt = 0
for p in P:
  for k in range(-K,K+1):
    i = p+k
    if(0<=i<N and H[i]==1):
      H[i]=0
      cnt+=1
      break
print(cnt)