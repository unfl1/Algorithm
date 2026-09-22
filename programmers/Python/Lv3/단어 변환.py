from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)

    dq = deque()
    dq.append((begin, 0))

    while dq:
        cur, chg = dq.popleft()

        if cur == target:
            return chg

        for idx, w in enumerate(words):
            if visited[idx]:
                continue

            cnt = 0

            # 현재 단어와 w가 몇 글자 다른지 확인
            for i in range(len(w)):
                if w[i] != cur[i]:
                    cnt += 1

            # 한 글자만 다르면 다음 단어로 이동 가능
            if cnt == 1:
                visited[idx] = True
                dq.append((w, chg + 1))

    return 0