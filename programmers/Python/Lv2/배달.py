import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    INF = 1e9
    dist = [INF] * (N + 1)
    dist[1] = 0

    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:
        cost, now = heapq.heappop(pq)

        if dist[now] < cost:
            continue

        for nxt, weight in graph[now]:
            new_cost = cost + weight

            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    answer = 0

    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1

    return answer