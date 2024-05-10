def solution(numbers):
    Num = set()
    
    def comb(Num,pick,unpick):
        if(pick!=''):
            Num|={int(pick)}
        for i in range(len(unpick)):
            comb(Num,pick+unpick[i], unpick[:i]+unpick[i+1:])
    
    comb(Num,'',numbers)
    Num-={0,1}
    for i in range(2,int(max(Num)**0.5)+1):
        Num-=set(range(i*2,max(Num)+1,i))
    return len(Num)