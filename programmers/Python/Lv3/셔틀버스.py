def solution(n, t, m, timetable):
    tt = sorted(to_minute(time) for time in timetable)
    start = to_minute("09:00")
    cur = 0

    for i in range(n):
        departure = start + t*i
        cnt = 0

        while cur < len(tt) and tt[cur] <= departure and cnt < m:
            cnt += 1
            cur += 1

        if i == n-1:
            if cnt < m:
                return to_time(departure)

            return to_time(tt[cur-1] - 1)

def to_minute(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def to_time(time):
    h = time // 60
    m = time % 60
    return f"{h:02d}:{m:02d}"