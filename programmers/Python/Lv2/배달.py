import heapq

def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range(N+1)]
    
    for i in range(len(road)):
        a=road[i][0]
        b=road[i][1]
        c=road[i][2]
        
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    distance = dijkstra(1, N, graph)
    
    for i in range(1, N+1):
        if distance[i]<=K:
            answer+=1
            
    return answer

def dijkstra(start, N, graph):
    INF = int(1e9)
    distance = [INF] * (N+1)
    
    pq = []
    
    heapq.heappush(pq, (0, start))
    distance[start]=0
    
    while pq:
        cur_dist, cur = heapq.heappop(pq)
        
        if distance[cur] < cur_dist:
            continue
            
        for nxt, cost in graph[cur]:
            nxt_dist = cur_dist + cost
            
            if nxt_dist<distance[nxt]:
                distance[nxt]=nxt_dist
                heapq.heappush(pq, (nxt_dist, nxt))
                
    return distance