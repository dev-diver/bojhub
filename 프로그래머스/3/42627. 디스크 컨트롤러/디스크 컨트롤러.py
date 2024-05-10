import heapq
def solution(jobs):
    N=len(jobs)
    jobs = sorted([(x[1],x[0]) for x in jobs], key = lambda x:x[1], reverse = True)
    requests = []
    time, answer = 0, 0
    while jobs or requests:
        while(jobs and jobs[-1][1]<=time):
            heapq.heappush(requests, jobs.pop())
        if(requests):
            req = heapq.heappop(requests)
            time += req[0]
            answer += time-req[1]
        else:
        	time+=1
    answer = answer//N
    return answer

