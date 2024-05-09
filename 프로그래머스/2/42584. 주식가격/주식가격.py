def solution(prices):
    answer = [0]*len(prices)
    stk=[]
    for idx, elem in enumerate(prices):
        while(stk and stk[-1][0]>elem):
            sElem = stk.pop()
            answer[sElem[1]]=idx-sElem[1]
        stk.append((elem,idx))
    for elem in stk:
        answer[elem[1]]=len(answer)-elem[1]-1
    return answer