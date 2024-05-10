
def solution(answers):
    pattern=[]
    pattern.append([1,2,3,4,5])
    pattern.append([2,1,2,3,2,4,2,5])
    pattern.append([3,3,1,1,2,2,4,4,5,5])
    
    answer = []
    cnt = [0,0,0]
    for i in range(len(answers)):
        for j in range(len(cnt)):
            cnt[j]+=1 if pattern[j][i%len(pattern[j])]==answers[i] else 0
    
    maxAns = max(cnt)
    
    for i in range(3):
        if(cnt[i]==maxAns):
            answer.append(i+1)
    return answer