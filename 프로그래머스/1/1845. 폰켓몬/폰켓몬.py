def solution(nums):
    N = len(nums)
    pick = N//2
    s = set(nums)
    return min(pick,len(s))

