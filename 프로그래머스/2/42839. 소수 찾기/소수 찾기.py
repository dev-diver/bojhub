def solution(numbers):
    Num = set()
    
    def comb(pick,unpick):
        if(pick!=''):
            Num.add(int(pick))
        for i in range(len(unpick)):
            comb(pick+unpick[i], unpick[:i]+unpick[i+1:])
            
    comb('',numbers)
    Num-={0,1}
    for i in range(2,int(max(Num)**0.5)+1):
        Num-=set(range(i*2,max(Num)+1,i))
    return len(Num)