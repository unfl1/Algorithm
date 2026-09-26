visited = []
ans = 0

def solution(k, dungeons):
    global visited, ans
    visited = [False] * len(dungeons)
    ans=0
    
    dfs (k, 0, dungeons)
    
    return ans

def dfs(cur, cnt, dungeons):
    global ans
    
    if cnt>ans:
        ans=cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and cur>=dungeons[i][0]:
            visited[i]=True
            dfs(cur-dungeons[i][1], cnt+1, dungeons)
            visited[i]=False