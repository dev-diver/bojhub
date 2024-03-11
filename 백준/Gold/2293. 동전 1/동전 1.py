N, K = map(int, input().split())
C = [int(input()) for _ in range(N)]

way = [0 for _ in range(K+1)]
way[0] = 1
for c in C:
    for i in range(c, K+1):
        way[i] += way[i-c]

print(way[K])