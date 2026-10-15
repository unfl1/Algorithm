from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    q = deque(truck_weights)
    second = 0
    total = 0
    
    while bridge:
        second+=1
        total -= bridge.popleft()
        
        if q:
            if total+q[0]<=weight:
                truck = q.popleft()
                bridge.append(truck)
                total += truck
            else:
                bridge.append(0)
            
    return second