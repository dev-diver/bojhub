import sys
input = sys.stdin.readline
N,K = map(int,input().split())
I = [[*map(int, input().split())] for _ in range(N)] #W, V
I = [[0,0]]+I
MaxV=K+1
memo = [[0]*len(I) for _ in range(MaxV)]

for capacity in range(K+1):
    for itemIdx in range(1,len(I)): 
        capI=capacity%MaxV
        if itemIdx > 0:
            r = memo[capI][itemIdx-1] #아이템 안 썼을 때
        restCap = capacity - I[itemIdx][0]
        if  restCap >=0 :
            #아이템 썼을 때랑 비교
            r = max(r,I[itemIdx][1]+memo[restCap%MaxV][itemIdx-1])
        memo[capI][itemIdx]=r

print(memo[K%MaxV][len(I)-1])