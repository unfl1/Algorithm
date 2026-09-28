def solution(topping):
    answer = 0
    
    total = {}
    left = set()
    
    for t in topping:
        total[t] = total.get(t,0)+1
    
    for t in topping:
        left.add(t)
        total[t]-=1
        
        if total[t]==0:
            del(total[t])
        
        if len(left)==len(total):
            answer+=1
            
    return answer