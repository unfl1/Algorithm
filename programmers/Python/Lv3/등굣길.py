def solution(m, n, puddles):
    
    board = [[-1]*m for _ in range(n)]

    for p in puddles:
        board[p[1]-1][p[0]-1]=0
        
    board[0][0]=1
        
    for i in range(n):
        for j in range(m):
            if board[i][j]==-1:
                if i==0:
                    board[i][j]=board[i][j-1]
                elif j==0:
                    board[i][j]=board[i-1][j]
                else:
                    board[i][j]=(board[i-1][j]+board[i][j-1])%1000000007
    
    return board[n-1][m-1]