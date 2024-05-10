from itertools import permutations

def solution(numbers):
    
    MAX=int(1e4)
    Num = [True]*MAX
    Num[0], Num[1] = False, False
    primes=[]
    
    answer = 0
    for i in range(2,MAX):
        if(Num[i]==True):
            primes.append(i)
            k=2
            while(i*k<MAX):
                Num[i*k]=False
                k+=1
    
    nums = [*numbers]
    combs = set()
    for l in range(1,len(nums)+1):
        for perm in permutations(nums,l):
            combs.add(int(''.join(perm)))
            
    def isPrime(N):
        for p in primes:
            if(N%p==0):
                return False
        return True
    
    for c in combs:
        try:
            if(Num[c]):
                answer+=1
        except IndexError:
            if(isPrime(c)):
                answer+=1
    return answer