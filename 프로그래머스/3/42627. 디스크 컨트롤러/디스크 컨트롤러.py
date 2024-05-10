import heapq
from collections import deque
def solution(jobs):
    N=len(jobs)
    answer = 0
    jobs.sort(key = lambda x:x[0])
    jobs = deque(jobs)
    requests = []
    time = 0
    while jobs:
        while(jobs and jobs[0][0]<=time):
            startTime,workTime = jobs.popleft()
            heapq.heappush(requests, (workTime,startTime))
        if(requests):
            req = heapq.heappop(requests)
            time += req[0]
            answer += time-req[1]
        else:
        	time+=1
    while(requests):
        req = heapq.heappop(requests)
        time += req[0]
        answer += time-req[1]
    answer = answer//N
    return answer

