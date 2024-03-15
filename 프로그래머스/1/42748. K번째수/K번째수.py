def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        ans = sorted(array[i-1:j])[k-1]
        answer.append(ans)
    #print("answer")
    return answer