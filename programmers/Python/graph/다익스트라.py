# ============================================================
# 문제
# ------------------------------------------------------------
# N개의 도시와 M개의 단방향 도로가 있다.
# 각 도로에는 이동 비용이 존재한다.
# 시작 도시에서 다른 모든 도시까지의 최단 거리를 구하시오.

# 입력
# 첫째 줄: 도시 개수 N, 도로 개수 M
# 둘째 줄: 시작 도시 start
# 이후 M개의 줄:
#   출발 도시, 도착 도시, 이동 비용

# 예제 입력
# 5 6
# 1
# 1 2 2
# 1 3 5
# 2 3 1
# 2 4 2
# 3 4 3
# 4 5 1

# 예제 출력
# 0
# 2
# 3
# 4
# 5
#
# ============================================================

import heapq

N, M = map(int, input().split())

start = int(input())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    INF = int(1e9)

    # 현 위치에서 갈 수 있는 거리는 무한으로 초기화
    dist = [INF] * (N+1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur = heapq.heappop(pq)

        # 현재 cost가 최소 거리보다 작으면 스킵
        if cur_cost > dist[cur]:
            continue

        # 현재 장소와 연결된 다른 장소들 탐색
        for nxt, nxt_cost in graph[cur]:
            nxt_dist = cur_cost + nxt_cost

            if (nxt_dist < dist[nxt]):
                dist[nxt] = nxt_dist
                heapq.heappush(pq, (nxt_dist, nxt))

    return dist

distance = dijkstra(start)

for i in range(1, N+1):
    print(distance[i])