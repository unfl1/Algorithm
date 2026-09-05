import heapq

def solution(scoville, K):
    answer = 0
    hq=[]
    for i in scoville:
        heapq.heappush(hq,i)

    while (hq[0]<K):
        if len(hq)<2:
            return -1
        
        heapq.heappush(hq,heapq.heappop(hq)+heapq.heappop(hq)*2)
        answer+=1

    return answer