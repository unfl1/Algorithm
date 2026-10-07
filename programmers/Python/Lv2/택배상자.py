def solution(order):
    cur = 0
    stack = []
    
    for i in range(len(order)):
        if order[cur] == i+1:
            cur+=1
        else:
            stack.append(i+1)
        
        while stack and stack[-1]==order[cur]:
            stack.pop()
            cur+=1
        
    return cur