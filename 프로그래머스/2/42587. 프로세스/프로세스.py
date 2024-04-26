from collections import deque
def solution(priorities, location):
    Q=deque([(i,p) for i,p in enumerate(priorities)])
    D=[0 for _ in range(9)]
    for i,p in enumerate(priorities):
        D[p-1]+=1
    maxp=0
    for i in range(9):
        if(D[i]>0):
            maxp = i+1
            
    k=0
    while Q:
        i,p = Q.popleft()
        if p<maxp:
            Q.append((i,p))
        else:
            k+=1
            D[p-1]-=1
            if(D[p-1]==0):
                for j in range(p-2,-1,-1):
                    if(D[j]>0):
                        maxp = j+1
                        break
            if(i==location):
                break
    return k