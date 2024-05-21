def solution(n, lost, reserve):
    
    res = set(reserve)
    answer = n-len(lost)
    
    for student in lost:
        if(student in reserve):
            res.remove(student)
    
    lost.sort()
    for student in lost:
        if student in reserve:
            answer+=1
            continue
        if student-1 in res:
            res.remove(student-1)
            answer+=1
            continue
        elif student+1 in res:
            res.remove(student+1)
            answer+=1
            continue
    return answer