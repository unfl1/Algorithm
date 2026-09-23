import heapq

def solution(operations):
    max_pq = []
    min_pq = []
    
    for op in operations:
        a, b = op.split()
        
        if a=="I":
            heapq.heappush(max_pq, -int(b))
            heapq.heappush(min_pq, int(b))
            
        elif a=="D":
            if b=="1":
                if max_pq:
                    val = -heapq.heappop(max_pq)
                    min_pq.remove(val)
                    heapq.heapify(min_pq)
            else:
                if min_pq:
                    val = -heapq.heappop(min_pq)
                    max_pq.remove(val)
                    heapq.heapify(max_pq)
                    
    if min_pq:
        return [max(min_pq), min(min_pq)]
    else:
        return [0,0]