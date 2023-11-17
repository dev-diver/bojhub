S=[*str(int(input())*int(input())*int(input()))]
cnt=[0]*10
for s in S:
    cnt[int(s)]+=1
print(*cnt, sep="\n")