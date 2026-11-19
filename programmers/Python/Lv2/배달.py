import heapq

def solution(N, road, K):
    
    graph = [[] for _ in range(N+1)]
    
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        
    dist = [int(1e9)] * (N+1)
    dist[1] = 0
    
    pq = []
    heapq.heappush(pq, (0, 1))
    
    while pq:
        cur_cost, cur = heapq.heappop(pq)
        
        if dist[cur] < cur_cost:
            continue
            
        for nxt, nxt_cost in graph[cur]:
            new_cost = cur_cost + nxt_cost
            
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
                
    ans = 0            
                
    for i in range(1, N+1):
        if dist[i] <= K:
            ans+=1

    return ans