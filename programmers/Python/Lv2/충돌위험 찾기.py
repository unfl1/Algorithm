def solution(points, routes):
    answer = 0

    # 포인트 번호 → 좌표
    positions = {i: (r, c) for i, (r, c) in enumerate(points, start=1)}

    # 로봇 상태: [현재 r, 현재 c, 다음 목적지]
    robots = []
    for route in routes:
        r, c = positions[route[0]]
        robots.append([r, c, 1])

    answer += check(robots)

    while any(robot is not None for robot in robots):
        for i in range(len(robots)):
            if robots[i] is None:
                continue

            r, c, target_idx = robots[i]

            # 마지막 목적지에 도착한 로봇 제거
            if target_idx == len(routes[i]):
                robots[i] = None
                continue

            target_r, target_c = positions[routes[i][target_idx]]

            # r 좌표 먼저
            if r < target_r:
                r += 1
            elif r > target_r:
                r -= 1
            elif c < target_c:
                c += 1
            elif c > target_c:
                c -= 1

            # 목적지에 도착하면 -> 다음 목적지
            if r == target_r and c == target_c:
                target_idx += 1

            robots[i] = [r, c, target_idx]

        # 충돌 확인
        answer += check(robots)

    return answer


def check(robots):
    counts = {}

    for robot in robots:
        if robot is None:
            continue

        r, c, _ = robot
        pos = (r, c)

        counts[pos] = counts.get(pos, 0) + 1

    result = 0

    for count in counts.values():
        if count >= 2:
            result += 1

    return result