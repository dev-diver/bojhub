from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time=0
    bridge = deque([])
    truck_weights = deque(truck_weights)
    while(truck_weights):
        time+=1
        if(bridge and time-bridge_length>=bridge[0][0]):
            bridge.popleft()
        if(sum([elem[1] for elem in bridge]) + truck_weights[0]<=weight):
            truck = truck_weights.popleft()
            bridge.append((time,truck))
    answer = time + bridge_length
    return answer