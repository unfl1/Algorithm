def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    answer = 0
    cur_d, cur_p = 0, 0

    while cur_d < n or cur_p < n:
        while cur_d < n and deliveries[cur_d] == 0:
            cur_d += 1

        while cur_p < n and pickups[cur_p] == 0:
            cur_p += 1

        if cur_d == n and cur_p == n:
            break

        dist = min(cur_d, cur_p)
        answer += (n - dist) * 2

        cur_d = process(deliveries, cur_d, cap, n)
        cur_p = process(pickups, cur_p, cap, n)

    return answer

def process(arr, idx, cap, n):
    remain = cap

    while idx < n and remain > 0:
        count = min(remain, arr[idx])
        arr[idx] -= count
        remain -= count

        if arr[idx] == 0:
            idx += 1

    return idx