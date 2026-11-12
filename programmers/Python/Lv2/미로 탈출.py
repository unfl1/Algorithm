from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def is_range(y, x, graph):
    return y>=0 and y<len(graph) and x>=0 and x<len(graph[0])


def bfs (sy, sx, ty, tx, graph):
    
    visited = [[-1] * len(graph[0]) for _ in range(len(graph))]
    
    dq = deque()
    dq.append((sy, sx))
    visited[sy][sx] = 0
    
    while dq:
        cur_y, cur_x = dq.popleft()
        
        for d in range(4):
            ny = cur_y + dy[d]
            nx = cur_x + dx[d]
            
            if is_range(ny, nx, graph) and graph[ny][nx]!="X" and visited[ny][nx]==-1:
                visited[ny][nx] = visited[cur_y][cur_x]+1
                dq.append((ny, nx))
                
    return visited[ty][tx]


def solution(maps):
    answer = 0
    
    sy, sx, ly, lx, ey, ex = 0, 0, 0, 0, 0, 0
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x]=="S":
                sy = y
                sx = x
            if maps[y][x]=="L":
                ly = y
                lx = x
            if maps[y][x]=="E":
                ey = y
                ex = x
                
    to_L = bfs(sy, sx, ly, lx, maps)
    to_E = bfs(ly, lx, ey, ex, maps)
    
    return -1 if to_L == -1 or to_E == -1 else to_L + to_E