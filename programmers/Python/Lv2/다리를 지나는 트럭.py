from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    dq=deque([0]*bridge_length)
    idx=0

    while idx<len(truck_weights):
        # 1초 지나면 다리 맨 앞칸이 빔
        dq.popleft()

        # 현재 트럭이 다리에 올라가도 무게 제한 X
        if sum(dq)+truck_weights[idx]<=weight:
            dq.append(truck_weights[idx])
            idx+=1
            
        # 무게 제한에 걸림
        else:
            dq.append(0)

        time+=1

    # 마지막 트럭이 지나가는 시간
    time += bridge_length

    return time