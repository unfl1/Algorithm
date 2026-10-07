from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    cnt=0
    limit = (len(q1) + len(q2)) * 2
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    
    if (sum_q1 + sum_q2) % 2 != 0:
        return -1
    
    while cnt < limit:
        if sum_q1 == sum_q2:
            break
        
        while sum_q1 > sum_q2:
            val = q1.popleft()
            q2.append(val)
            sum_q1-=val
            sum_q2+=val
            cnt+=1
            
        while sum_q2 > sum_q1:
            val = q2.popleft()
            q1.append(val)
            sum_q2-=val
            sum_q1+=val
            cnt+=1
        
    return -1 if cnt >= limit else cnt 