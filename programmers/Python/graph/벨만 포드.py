# ============================================================
# 문제
# ------------------------------------------------------------
# N개의 도시와 M개의 단방향 도로가 있다.
# 각 도로에는 이동 비용이 존재하며, 이동 비용은 음수일 수도 있다.
# 주어진 시작 도시에서 다른 모든 도시까지의 최단 거리를 구하시오.
# 단, 시작 도시에서 도달할 수 있는 음수 사이클이 존재하면 -1을 출력한다.

# 입력
# 첫째 줄: 도시 개수 N, 도로 개수 M
# 둘째 줄: 시작 도시
# 이후 M개의 줄:
#   출발 도시, 도착 도시, 이동 비용

# 예제 입력
# 4 5
# 1
# 1 2 4
# 1 3 3
# 2 3 -2
# 3 4 2
# 4 2 -5

# 예제 출력
# -1
#
# ============================================================

INF = int(1e9)

N, M = map(int, input().split())

start = int(input())

graph = []

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph.append((a, b, cost))

def bellman_ford(start):
    distance = [INF] * (N+1)
    distance[start] = 0

    for i in range(N):
        for cur, nxt, cost in graph:
            if distance[cur] == INF:
                continue

            new_dist = distance[cur] + cost

            if new_dist < distance[nxt]:
                distance[nxt] = new_dist

                if i == N-1:
                    return None

    return distance

distance = bellman_ford(start)

if distance is None:
    print(-1)
else:
    for i in range(1, N+1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])