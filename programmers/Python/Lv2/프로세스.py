from collections import deque

def solution(priorities, location):
    answer = 0
    dq=deque()
    prio_dq=deque(sorted(priorities, reverse = True))
    
    for idx, value in enumerate(priorities):
        dq.append((value, idx))    
        
    while dq:
        cur_v, cur_i = dq.popleft()
        
        if cur_v == prio_dq[0]:
            answer+=1
            prio_dq.popleft()
            if cur_i==location:
                return answer
        else:
            dq.append((cur_v, cur_i))