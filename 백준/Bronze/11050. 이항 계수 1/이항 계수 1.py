N,K=map(int,input().split())
fact = [1]*11
for i in range(1,11):
  fact[i]=fact[i-1]*i
print(fact[N]//fact[K]//fact[N-K])