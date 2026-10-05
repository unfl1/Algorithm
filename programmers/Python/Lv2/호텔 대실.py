import heapq

def solution(book_time):
    book_time.sort()
    hotel=[]
    
    for start, end in book_time:
        start = to_minute(start)
        end = to_minute(end)
        
        # 가장 빨리 비는 방 재사용
        if hotel and hotel[0]<=start:
            heapq.heappop(hotel)
            
        heapq.heappush(hotel, end+10)
        
    return len(hotel)

def to_minute(t):
    h,m = map(int, t.split(":"))
    return h*60 + m