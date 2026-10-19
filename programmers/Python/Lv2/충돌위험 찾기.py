def solution(points, routes):
    answer = 0
    
    pos = {i:(r,c) for i, (r,c) in enumerate(points, start=1)}

    # r, c, 다음 목적지 idx
    robots = []
    for route in routes:
        r,c = pos[route[0]]
        robots.append([r, c, 1])
        
    answer += check(robots)
        
    while any(robot is not None for robot in robots):
        for i in range(len(robots)):
            if robots[i] is None:
                continue
                
            r, c, target_idx = robots[i]
            
            # 마지막 목적지 도착 로봇 제거
            if target_idx == len(routes[i]):
                robots[i] = None
                continue
                
            target_r, target_c = pos[routes[i][target_idx]]
            
            # r좌표 먼저
            if r < target_r:
                r+=1
            elif r > target_r:
                r-=1
            elif c < target_c:
                c+=1
            elif c > target_c:
                c-=1
                
            # 목적지 도착하면 다음 목적지
            if r == target_r and c == target_c:
                target_idx+=1
                
            robots[i] = [r, c, target_idx]
        
        # 충돌 확인
        answer += check(robots)
            
    return answer

def check(robots):
    pos = {}
    cnt=0
    
    for robot in robots:
        if robot is None:
            continue
            
        r, c, _ = robot
        
        pos[(r,c)] = pos.get((r,c), 0) + 1
        
    for p in pos:
        if pos[p]>=2:
            cnt+=1
            
    return cnt