from collections import defaultdict
def solution(participant, completion):
    d = defaultdict(int)
    for p in participant: d[p]+=1
    for c in completion: d[c]-=1
    return [x for x in d if d[x]!=0][0]