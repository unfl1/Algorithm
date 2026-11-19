from collections import deque

def solution(players, m, k):
    answer = 0
    
    dq = deque([0] * k)
    
    for player in players:
        dq.popleft()
        server = player // m
        now = sum(dq)
        
        if now < server:
            req = server-now
            dq.append(req)
            answer+=req
        else:
            dq.append(0)
            
    return answer