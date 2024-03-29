def isNext(src, dst):
    diff = 0
    for i,c in enumerate(src):
        if(c!=dst[i]):
            diff+=1
        if(diff>1): return False
    return True


def solution(begin, target, words):
    
    visited = set()
    visited.add(begin)
    stack = [(begin,0)]
    
    while stack:
        src, s = stack.pop()
        if(src == target):
            return s
        
        for word in words:
            if((not word in visited) and isNext(src, word)):
                visited.add(word)
                stack.append((word, s+1))
                
    return 0