import heapq
def solution(word):
    D=[]
    def make(str1):
        if(str1!=''):
            heapq.heappush(D,str1)
        if(len(str1)==5): return
        for c in 'AEIOU':
            make(str1+c)
    make('')
    cnt=1
    while(D[0]!=word):
        heapq.heappop(D)
        cnt+=1
    return cnt