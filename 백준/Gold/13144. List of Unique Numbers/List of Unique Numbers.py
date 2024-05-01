import sys
input = sys.stdin.readline
N = int(input())
*S, = map(int, input().split())

def comb(n):
    return n*(n-1)//2 + n

i = 0
j = 0
nums = set()
s = 0
while(j<N):
    if S[j] in nums:
        s+=comb(j-i)
        # print(i,j,"+",comb(j-i))
        while(S[i]!=S[j]):
            nums.remove(S[i])
            i+=1
        i+=1
        s-=comb(j-i)
        # print(i,j,"-",comb(j-i))
    nums.add(S[j])
    j+=1
s+=comb(j-i)
# print(i,j,"+",comb(j-i))
print(s)
