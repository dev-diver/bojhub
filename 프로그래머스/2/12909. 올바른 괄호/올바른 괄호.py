def solution(s):
    answer = True
    stk=[]
    for c in s:
        if(c=="("):
            stk.append(c)
        else:
            if(stk and stk[-1]=="("):
                stk.pop()
            else:
                answer = False
                break
    if stk:
        answer = False
    return answer 