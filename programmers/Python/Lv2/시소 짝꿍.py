def solution(weights):
    answer = 0
    count = {}

    for w in sorted(weights):
        # 같은 무게
        answer += count.get(w, 0)

        # 현재 사람이 더 무거운 경우
        if w % 2 == 0:
            answer += count.get(w // 2, 0)

        if w % 3 == 0:
            answer += count.get(w * 2 // 3, 0)

        if w % 4 == 0:
            answer += count.get(w * 3 // 4, 0)

        count[w] = count.get(w, 0) + 1

    return answer