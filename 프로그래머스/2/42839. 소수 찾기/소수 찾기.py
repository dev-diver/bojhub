from itertools import permutations
def solution(numbers):
    Num = set()
    numbers = [*numbers]
    for i in range(len(numbers)):
        for perm in permutations(numbers,i+1):
            Num|={int(''.join(perm))}
    Num-={0,1}
    for i in range(2,int(max(Num)**0.5)+1):
        Num-=set(range(i*2,max(Num)+1,i))
    return len(Num)