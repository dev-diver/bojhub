import sys
input = sys.stdin.readline

def makePay(amount, coinIdx): #남은 금액에 대해,n번째 코인을 쓰는 경우의 수
    if amount ==0:
        return 1 # 한가지 경우가 만들어짐
    if amount < 0 or coinIdx<=0:
        return 0 # 안 만들어짐
    if memo[amount][coinIdx]!=-1:
        return memo[amount][coinIdx]
    use_coin = makePay(amount-coins[coinIdx],coinIdx) #쓴 경우, 하나 더 쓸 수 있나 시험
    not_use_coin = makePay(amount,coinIdx-1) # 못 쓴 경우, 같은 금액에 대해 다음 작은 코인으로 패스
    r = use_coin + not_use_coin
    memo[amount][coinIdx] = r
    return r

T = int(input())
for _ in range(T):
    N = int(input()) #코인의 수
    coins = [0] +[*map(int, input().split())]
    M = int(input()) #총액
    memo = [[-1]*(N+1) for _ in range(M+1)] #절대 올수 없는 수, -1로 초기화
    print(makePay(M, N))
