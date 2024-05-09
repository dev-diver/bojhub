def solution(arr):
    
    answer = []
    prevElem = -1
    for elem in arr:
        if(elem!=prevElem):
            answer.append(elem)
            prevElem=elem

    return answer