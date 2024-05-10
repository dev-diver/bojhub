def one(i):
    return i%5+1

def two(i):
    if(i%2==0):
        return 2
    else:
        i=i%8
        if(i==1):
            return 1
        elif(i==3):
            return 3
        elif(i==5):
            return 4
        elif(i==7):
            return 5

def three(i):
    i=i%10
    i=i//2
    if(i==0):
    	return 3
    elif(i==1):
    	return 1
    elif(i==2):
    	return 2
    elif(i==3):
    	return 4
    elif(i==4):
        return 5
    
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