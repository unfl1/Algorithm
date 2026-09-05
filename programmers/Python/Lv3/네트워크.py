def solution(n, computers):
    cnt = 0

    network = [[] for _ in range(n)]
    visited = [False] * n

    # 인접리스트로 표현
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j]==1 and i!=j:
                network[i].append(j)

    # 네트워크
    def dfs(net):
        if visited[net]:
            return

        visited[net]=True

        for i in network[net]:
            dfs(i)

    # 네트워크 개수
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt+=1
    
    return cnt