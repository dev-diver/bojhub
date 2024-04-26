def solution(citations):
    arr = [0]*10001
    for cite in citations:
        arr[cite]+=1
    for i in range(len(arr)-2,-1,-1):
        arr[i] = arr[i+1] + arr[i]
    ans=0
    for i in range(len(arr)-1,-1,-1):
        if(arr[i]>=i):
            ans=i
            break
    return ans