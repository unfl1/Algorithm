def solution(n):
    graph = [[0]*(i+1) for i in range(n)]
    # 방향
    dx=[1,0,-1]
    dy=[0,1,-1]
    x,y,d=0,0,0
    num=1
    graph[0][0]=1
    while num<n*(n+1)//2:
        nx=x+dx[d]
        ny=y+dy[d]
        if nx<0 or nx>=n or ny<0 or ny>=n or graph[nx][ny]!=0:
            d=(d+1)%3
        else:
            num+=1
            graph[nx][ny]=num
            x,y=nx,ny

    answer=[]
    for line in graph:
        answer.extend(line)
    return answer