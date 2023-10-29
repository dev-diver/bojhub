import sys

def coin_combinations(coins, current_coin, target_amount, memo):
    if target_amount == 0:
        return 1
    if target_amount < 0 or current_coin <= 0:
        return 0
    if (current_coin, target_amount) in memo:
        return memo[(current_coin, target_amount)]

    # 현재 동전을 사용하는 경우와 사용하지 않는 경우를 모두 고려
    use_coin = coin_combinations(coins, current_coin, target_amount - coins[current_coin], memo)
    dont_use_coin = coin_combinations(coins, current_coin - 1, target_amount, memo)
    memo[(current_coin, target_amount)] = use_coin + dont_use_coin

    return memo[(current_coin, target_amount)]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    coins.insert(0, 0)
    M = int(sys.stdin.readline())

    memo = {}
    print(coin_combinations(coins, N, M, memo))
