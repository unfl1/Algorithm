def dfs(start, graph, visited):
    if visited[start]:
        return 0

    visited[start] = True
    cnt = 1

    for nxt in graph[start]:
        cnt += dfs(nxt, graph, visited)

    return cnt


def solution(n, wires):
    answer = n

    for idx, (a, b) in enumerate(wires):
        graph = [[] for _ in range(n + 1)]

        for i, (u, v) in enumerate(wires):
            if i == idx:
                continue

            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)

        network1 = dfs(a, graph, visited)
        network2 = n - network1

        answer = min(answer, abs(network1 - network2))

    return answer
