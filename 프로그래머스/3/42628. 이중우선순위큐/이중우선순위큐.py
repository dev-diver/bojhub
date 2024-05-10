import heapq
from collections import defaultdict
def solution(operations):
    answer = []
    count = defaultdict(int)
    minQ = []
    maxQ = []
    for ops in operations:
        cmd,num = ops.split()
        if(cmd=='I'):
            num = int(num)
            heapq.heappush(minQ,num)
            heapq.heappush(maxQ,-num)
            count[num]+=1
        else: # 삭제
            if(num=='1'):
                while maxQ:
                    elem = -heapq.heappop(maxQ)
                    if(count[elem]>0):
                        count[elem]-=1
                        break
            else:
                while minQ:
                    elem = heapq.heappop(minQ)
                    if(count[elem]>0):
                        count[elem]-=1
                        break
    while maxQ and count[-maxQ[0]]==0:
        heapq.heappop(maxQ)
    while minQ and count[minQ[0]]==0:
        heapq.heappop(minQ)
    return [-maxQ[0],minQ[0]] if maxQ else [0,0]