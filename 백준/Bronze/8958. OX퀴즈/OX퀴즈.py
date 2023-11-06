import sys
input = sys.stdin.readline
N = int(input())
Q = [[*input().strip()] for _ in range(N)]
for q in Q:
    strike = 0
    score = 0
    for a in q:
        if(a=="O"):
            strike+=1
            score+=strike
        else:
            strike=0
    print(score)