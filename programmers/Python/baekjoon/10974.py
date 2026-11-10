# 1부터 N까지 모든 순열 출력

N = int(input())

visited = [False]*(N+1)

cur=[]

def dfs(d):
    if d==N:
        print(*cur)
        return

    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=True
            cur.append(i)

            dfs(d+1)

            visited[i]=False
            cur.pop()

dfs(0)