# ============================================================
# 문제
# ------------------------------------------------------------
# N개의 도시와 M개의 단방향 도로가 있다.
# 각 도로에는 이동 비용이 존재한다.
# 모든 도시에서 다른 모든 도시까지의 최단 거리를 구하시오.

# 입력
# 첫째 줄: 도시 개수 N, 도로 개수 M
# 이후 M개의 줄:
#   출발 도시, 도착 도시, 이동 비용

# 예제 입력
# 4 5
# 1 2 4
# 1 3 10
# 2 3 3
# 2 4 8
# 3 4 2

# 예제 출력
# 0 4 7 9
# INF 0 3 5
# INF INF 0 2
# INF INF INF 0
#
# ============================================================

INF = int(1e9)

N, M = map(int, input().split())

graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i]=0

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()