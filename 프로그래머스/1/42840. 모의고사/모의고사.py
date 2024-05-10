def one(i):
    return i%5+1

pattern2=[2,1,2,3,2,4,2,5,2]
def two(i):
    i=i%8
    return pattern2[i]

pattern3=[3,3,1,1,2,2,4,4,5,5]
def three(i):
    i=i%10
    return pattern3[i]
    
def solution(answers):
    answer = []
    cnt=[0,0,0]
    for i in range(len(answers)):
        cnt[0]+=1 if one(i)==answers[i] else 0
        cnt[1]+=1 if two(i)==answers[i] else 0
        cnt[2]+=1 if three(i)==answers[i] else 0
    maxAns = max(cnt)
    for i in range(3):
        if(cnt[i]==maxAns):
            answer.append(i+1)
    return answer