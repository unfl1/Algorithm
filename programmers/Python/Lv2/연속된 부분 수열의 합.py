def solution(sequence, k):
    ans = []
    
    left = 0
    right = -1
    cur = 0 # 현재 합
    
    while left < len(sequence):
        if cur > k :
            cur-=sequence[left]
            left+=1
            
        else:
            if cur == k:
                ans.append((left, right))

            right+=1
            
            if right>=len(sequence):
                break
                
            cur+=sequence[right]
    
    ans.sort(key = lambda x: (x[1]-x[0], x[0]))
    
    return ans[0]