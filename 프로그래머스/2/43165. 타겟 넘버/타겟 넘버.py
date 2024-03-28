def dfs(numbers, current_idx, s, target):
    if(current_idx == len(numbers)):
        if(s == target):
            return 1
        else: 
            return 0
    cnt = 0
    for next_node in [numbers[current_idx], -numbers[current_idx]]:
        cnt += dfs(numbers, current_idx + 1, s + next_node, target)
    
    return cnt

def solution(numbers, target):
    
    return dfs(numbers, 0, 0, target)