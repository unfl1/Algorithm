def solution(n, s):
    
    if s<n:
        return [-1]
    
    numbers= [s//n]*n
    
    s%=n
    
    for i in range(s):
        numbers[i]+=1
        
    return sorted(numbers)