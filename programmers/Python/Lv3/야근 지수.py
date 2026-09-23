import heapq

def solution(n, works):
    answer = 0
    
    pq = []
    for work in works:
        heapq.heappush(pq, -work)
    
    while n!=0 and len(pq)!=0:
        cur = -heapq.heappop(pq)
        
        if cur != 0:
            heapq.heappush(pq, -(cur-1))
        
        n-=1
        
    if len(pq)==0:
        return 0
    else:
        while pq:
            answer+=heapq.heappop(pq)**2
            
        return answer