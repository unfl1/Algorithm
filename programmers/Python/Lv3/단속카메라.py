def solution(routes):
    
    routes = sorted(routes, key = lambda x: x[1])
    camera = 0
    cur = -30001
    
    for a, b in routes:
        if a > cur:
            cur = b
            camera += 1
            
    return camera