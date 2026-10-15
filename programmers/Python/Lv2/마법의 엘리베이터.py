def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))

    for i in range(len(storey)-1, 0, -1):
        cur = storey[i]
        nxt = storey[i-1]

        if cur < 5 or (cur == 5 and nxt < 5):
            answer += cur
            storey[i] = 0
        else:
            answer += 10 - cur
            storey[i-1] += 1

    answer += min(storey[0], 11 - storey[0])

    return answer