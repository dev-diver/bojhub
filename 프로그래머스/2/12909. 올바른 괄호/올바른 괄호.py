def solution(s):
    stk=[]
    for c in s:
        if(c=="("):
            stk.append(c)
        else:
            try:
                stk.pop()
            except IndexError:
                return False
    return False if stk else True 