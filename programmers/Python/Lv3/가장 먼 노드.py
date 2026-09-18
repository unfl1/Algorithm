from collections import deque

INF = int(1e9)

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    
    dist = [INF] * (n+1)
    
    dist[1]=0
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    dq = deque()
    dq.append((1,0))
    
    while dq:
        cur, cur_dist=dq.popleft()
        
        for nxt in graph[cur]:
            if dist[nxt]==INF:
                dist[nxt]=cur_dist+1
                dq.append((nxt, dist[nxt]))
    
    dist[0]=0
    
    max_dist = max(dist)

    for i in range(1, n+1):
        if dist[i] == max_dist:
            answer += 1
            
    return answer