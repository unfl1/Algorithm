def solution(n, stations, w):
    answer = 0
    cur = 1
    camera_range = 2*w + 1

    for station in stations:
        start = max(1, station-w)
        end = min(n, station+w)

        if cur < start:
            answer += (start-cur+camera_range-1)//camera_range

        cur = end + 1

    if cur <= n:
        answer += (n-cur+1+camera_range-1)//camera_range

    return answer