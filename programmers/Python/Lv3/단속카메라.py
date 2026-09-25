def solution(routes):
    routes.sort(key = lambda x : x[1])
    camera = []
    
    for start, end in routes:
        if len(camera)==0:
            camera.append(end)
        elif start<=camera[-1]<=end:
            continue
        else:
            camera.append(end)
            
    return len(camera)