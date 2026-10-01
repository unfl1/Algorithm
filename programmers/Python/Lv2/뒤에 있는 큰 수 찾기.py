class Num:
    def __init__(self, idx, value):
        self.idx=idx
        self.value=value

def solution(numbers):
    answer = [0] * len(numbers)
    
    stack=[]
    
    for idx, value in enumerate(numbers):
        while stack and stack[-1].value<value:
            cur = stack.pop()
            answer[cur.idx] = value
        
        stack.append(Num(idx, value))
                
    if stack:
        for num in stack:
            answer[num.idx] = -1
            
    return answer