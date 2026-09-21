import heapq

INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for start, end, cost in fares:
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    dist_s = dijkstra(s, n, graph)
    dist_a = dijkstra(a, n, graph)
    dist_b = dijkstra(b, n, graph)

    answer = INF

    for k in range(1, n + 1):
        answer = min(
            answer,
            dist_s[k] + dist_a[k] + dist_b[k]
        )

    return answer


def dijkstra(start, n, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur = heapq.heappop(pq)

        if dist[cur] < cur_cost:
            continue

        for nxt, cost in graph[cur]:
            nxt_cost = cur_cost + cost

            if nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heapq.heappush(pq, (nxt_cost, nxt))

    return dist