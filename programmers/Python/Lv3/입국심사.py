def solution(n, times):
    answer = 0
    
    left=0
    right=n*max(times)
    
    while left<=right:
        mid = (left+right) // 2
        
        people=0
        
        for time in times:
            people += mid//time
            
        if n<=people:
            right=mid-1
            
        else:
            left=mid+1
            
    return right+1
    