import sys
input = sys.stdin.readline

def makePay(amount, coinIdx):
    if amount ==0:
        return 1
    if amount < 0 or coinIdx<=0:
        return 0
    if memo[amount][coinIdx]!=-1:
        return memo[amount][coinIdx]
    use_coin = makePay(amount-coins[coinIdx],coinIdx)
    not_use_coin = makePay(amount,coinIdx-1)
    r= use_coin + not_use_coin
    memo[amount][coinIdx] = r
    return r

T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0] +[*map(int, input().split())]
    M = int(input())

    memo = [[-1]*(N+1) for _ in range(M+1)]
    print(makePay(M, N))
