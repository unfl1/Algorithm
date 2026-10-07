from collections import deque

def solution(m, n, board):
    answer = 0
    
    board = [list(x) for x in board]
    
    while True:
        remove = set()
        
        # 1. 없어질 위치 찾기
        for y in range(m-1):
            for x in range(n-1):
                flag = True
                cur = board[y][x]
                
                if cur == " ":
                    continue
                
                for i in range(2):
                    for j in range(2):
                        if board[y+i][x+j] != cur:
                            flag = False
                            break
                            
                    if not flag:
                        break
                        
                if flag:
                    for i in range(2):
                        for j in range(2):
                            remove.add((y+i, x+j))
                            
        # 제거할 것이 없다면 종료
        if len(remove) == 0:
            break
            
        # 2. 제거하기
        for y, x in remove:
            board[y][x]=" "
            
        answer+=len(remove)
        
        # 3. 옮기기
        for x in range(n):
            dq = deque()
            for y in range(m-1,-1,-1):
                if board [y][x] == " ":
                    dq.append(y)
                elif dq:
                    cur = dq.popleft()
                    board[cur][x] = board[y][x]
                    board[y][x] = " "
                    dq.append(y)
                    
    return answer