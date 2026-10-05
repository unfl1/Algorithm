import math

class Car:
    def __init__(self, in_time, total, state):
        self.in_time=in_time
        self.total=total
        self.state=state

def solution(fees, records):
    park = {}
    for info in records:
        time, car_num, state = info.split()
        time=to_minute(time)
        
        if car_num not in park:
            park[car_num]=Car(time, 0, state)
        else:
            cur = park[car_num]
            
            if state == "OUT":
                cur.total += time - cur.in_time
            else:
                cur.in_time=time
                
            cur.state=state
            
    for key, value in park.items():
        if value.state == "IN":
            value.total+=to_minute("23:59")-value.in_time
    
    answer=[v.total for k,v in sorted(park.items(), key = lambda x: x[0])]
    for i in range(len(answer)):
        answer[i] = cost(answer[i], fees[0], fees[1], fees[2], fees[3])
    
    return answer

def to_minute(t):
    total = 0
    h, m = map(int, t.split(":"))
    return h*60 + m

def cost(total_time, b_time, b_fee, u_time, u_fee):
    if total_time <= b_time:
        return b_fee
    else:
        return b_fee + (math.ceil((total_time - b_time) / u_time) * u_fee)
    