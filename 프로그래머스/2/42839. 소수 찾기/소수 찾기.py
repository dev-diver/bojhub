from itertools import permutations

def solution(numbers):
    nums = [*numbers]
    combs = set()
    for l in range(1,len(nums)+1):
        for perm in permutations(nums,l):
            combs.add(int(''.join(perm)))
    
    MAX=max(combs)+1
    Num = [True]*MAX
    Num[0], Num[1] = False, False

    answer = 0
    for i in range(2,MAX):
        for k in range(i*2,MAX,i):
            Num[k]=False

    for c in combs:
        if(Num[c]):
            answer+=1
    return answer