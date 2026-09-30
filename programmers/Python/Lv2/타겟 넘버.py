answer=0

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, 0, numbers, target)
    return answer

def dfs(d, cur, numbers, target):
    global answer
    
    if d==len(numbers):
        if cur == target:
            answer+=1
        
        return
    
    # 더하거나
    dfs(d+1, cur+numbers[d], numbers, target)
    # 빼거나
    dfs(d+1, cur-numbers[d], numbers, target)
        