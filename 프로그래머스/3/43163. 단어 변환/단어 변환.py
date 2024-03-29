from collections import deque

def isNext(src, dst):
    diff = 0
    for w1,w2 in zip(src,dst):
        if(w1!=w2):
            diff+=1
        if(diff>1): return False
    return True


def solution(begin, target, words):
    
    visited = set()
    visited.add(begin)
    que = deque([(begin,0)])
    
    while que:
        src, s = que.popleft()
        if(src == target):
            return s
        
        for word in words:
            if((not word in visited) and isNext(src, word)):
                visited.add(word)
                que.append((word, s+1))
                
    return 0