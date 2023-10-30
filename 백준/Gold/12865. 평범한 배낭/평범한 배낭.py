import sys
input = sys.stdin.readline
N,K = map(int,input().split())
I = [[*map(int, input().split())] for _ in range(N)] #W, V
I = [[0,0]]+I
memo = [[-1]*(K+1) for _ in range(2)]

for itemIdx in range(len(I)):
    for capacity in range(K+1):  
        if capacity==0 or itemIdx==0:
            memo[itemIdx%2][capacity]=0
            continue
        ip=itemIdx%2
        r = memo[ip-1][capacity] #아이템 안 썼을 떄
        if capacity - I[itemIdx][0] >=0 :
            #아이템 썼을 때랑 비교
            r = max(r,I[itemIdx][1]+memo[ip-1][capacity - I[itemIdx][0]])
        memo[ip][capacity]=r

print(memo[len(I)%2-1][K])