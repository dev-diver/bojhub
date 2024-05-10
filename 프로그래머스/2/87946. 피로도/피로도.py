def solution(k, dungeons):
    def makePerm(make,last):
        if(len(last)==0):
            perms.append(make)
            return
        else:
            for i in range(len(last)):
                makePerm(make+[last[i]],last[:i]+last[i+1:])
    
    perms = []
    makePerm([],dungeons)
    
    mx = 0
    for perm in perms:
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