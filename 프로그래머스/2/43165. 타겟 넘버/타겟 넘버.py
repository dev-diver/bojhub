def solution(numbers, target):
    
    stk = []
    stk.append((numbers[0],0))
    stk.append((-numbers[0],0))
    N = len(numbers)
    
    cnt = 0
    while stk:
        s, i = stk.pop()
        if(i == N-1):
            if(s == target):
                cnt += 1
            continue
        for next_n in [numbers[i+1], -numbers[i+1]]:
            stk.append((s+next_n, i+1))
    
    return cnt