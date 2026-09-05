from collections import deque

def solution(priorities, location):
    answer = 0
    dq=deque()
    prio_dq=deque(sorted(priorities, reverse=True))

    for idx, value in enumerate(priorities):
        dq.append((value,idx))

    while dq:
        # 꺼내고
        cur_value, cur_idx = dq.popleft()
        # 우선순위가 가장 높다면
        if cur_value==prio_dq[0]:
            prio_dq.popleft()
            answer+=1

            if cur_idx==location:
                break

        # 아니라면
        else:
            dq.append((cur_value, cur_idx))

    return answer