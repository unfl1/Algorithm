def solution(people, limit):
    people.sort(reverse=True)
    
    answer = 0
    left=0
    right=len(people)-1
    
    while left<=right:
        if people[right]+people[left]<=limit:
            right-=1
            
        left+=1    
        answer+=1
            
    return answer