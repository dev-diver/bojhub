from itertools import permutations

def solution(k, dungeons):
    
    mx = 0
    for perm in permutations(dungeons, len(dungeons)):
        hp = k
        visit = 0
        for need,cost in perm:
            if(hp >= need):
                visit+=1
                hp-=cost
            else:
                break
        mx = max(mx,visit)
    return mx