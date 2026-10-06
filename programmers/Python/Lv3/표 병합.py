def solution(commands):
    board = [[""]*50 for _ in range(50)]  # 그룹의 값은 대표 셀에만 저장
    parent = [i for i in range(50*50)]    # 처음에는 모든 셀이 자기 자신을 대표로 가짐
    ans=[]
    
    for com in commands:
        command = com.split() 
        
        if command[0]=="UPDATE":
            if len(command)==4:
                UPDATE1(board, int(command[1]), int(command[2]), command[3], parent)
            else:
                UPDATE2(board, command[1], command[2])
                
        elif command[0]=="MERGE":
            MERGE(board, int(command[1]), int(command[2]), int(command[3]), int(command[4]), parent)
        elif command[0]=="UNMERGE":
            UNMERGE(board, int(command[1]), int(command[2]), parent)
        elif command[0]=="PRINT":
            PRINT(board, int(command[1]), int(command[2]), ans, parent)
        
    return ans

# 문제의 좌표를 1차원 번호로 변환
def to_idx(r, c, board):
    return (r-1)*len(board) + (c-1)

# 1차원 번호를 board의 좌표로 변환
def to_back(idx, board):
    return idx//len(board), idx%len(board)

def find(parent, x):
    if parent[x]!=x:  # 자기 자신이 대표가 아니면 부모를 따라감
        parent[x] = find(parent, parent[x])  # 찾은 대표로 직접 연결: 경로 압축
        
    return parent[x]

def UPDATE1(board, r, c, value, parent):
    root = find(parent, to_idx(r, c, board))  # 해당 셀의 그룹 대표 찾기
    cr, cc = to_back(root, board)
    board[cr][cc]=value  # 대표에 저장된 그룹의 값 변경
    
def UPDATE2(board, value1, value2):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == value1:
                board[i][j] = value2

def MERGE(board, r1, c1, r2, c2, parent):
    root_a = find(parent, to_idx(r1, c1, board))
    root_b = find(parent, to_idx(r2, c2, board))
    
    if root_a == root_b:  # 이미 같은 그룹이면 종료
        return
    
    ar, ac = to_back(root_a, board)
    br, bc = to_back(root_b, board)
    
    if board[ar][ac] == "":  # 첫 번째 그룹이 비어 있으면 두 번째 값 사용
        board[ar][ac] = board[br][bc]
    
    parent[root_b] = root_a  # 두 번째 그룹을 첫 번째 대표 아래로 연결
    
    board[br][bc] = ""  # 대표가 아니게 된 셀의 값 제거
    
def UNMERGE(board, r, c, parent):
    cur = find(parent, to_idx(r, c, board))
    cr, cc = to_back(cur, board)
    value = board[cr][cc]  # 분리 전에 그룹의 값 보관
    
    members=[]

    # 같은 그룹의 셀을 먼저 모두 수집
    for i in range(len(parent)):
        if find(parent, i) == cur:
            members.append(i)  
            
    for i in members:
        parent[i] = i  # 각 셀을 독립된 그룹으로 분리
        cr, cc = to_back(i, board)
        board[cr][cc] = ""  # 분리한 셀의 값 초기화
        
    board[r-1][c-1] = value  # 지정한 셀에만 기존 그룹의 값 유지
            
def PRINT(board, r, c, ans, parent):
    root = find(parent, to_idx(r, c, board))
    cr, cc = to_back(root, board)
    
    if board[cr][cc] == "":
        ans.append("EMPTY")
    else:
        ans.append(board[cr][cc])  # 대표에 저장된 그룹의 값 출력