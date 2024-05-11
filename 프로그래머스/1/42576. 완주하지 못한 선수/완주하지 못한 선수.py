from collections import Counter
def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    p-=c
    return [*p.keys()][0]