import sys
input = sys.stdin.readline
N=int(input())
T=[[*map(int,input().split())] for _ in range(N)]
for t in T:
    score = t[1:]
    mean = sum(score)/len(score)
    a = [*filter(lambda x:x>mean,score)]
    overMean = len(a)/len(score)*100
    print("{:.3f}%".format(overMean))
