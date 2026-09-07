def solution(distance, rocks, n):

    rocks.sort()

    # 바위 사이의 거리
    dist = []
    # 거리 저장
    dist.append(rocks[0] - 0)

    for i in range(len(rocks) - 1):
        dist.append(rocks[i + 1] - rocks[i])

    dist.append(distance - rocks[-1])

    # "바위를 n개까지 제거했을 때 만들 수 있는 최소 거리의 최댓값"
    left = 0
    right = distance

    while left <= right:

        # 이번에 가정할 최소 거리
        mid = (left + right) // 2

        # mid를 만족시키기 위해 제거해야 하는 바위 개수
        remove_rock = 0

        # 바위를 제거하면 인접한 거리들이 합쳐지므로 누적 거리 사용
        cur_dist = 0

        for d in dist:
            cur_dist += d

            # 아직 거리가 mid보다 짧다면 현재 바위를 제거
            if cur_dist < mid:
                remove_rock += 1

            # mid 이상 거리를 확보했다면 현재 바위는 남길 수 있으므로 여기서부터 다시 거리 계산
            else:
                cur_dist = 0

        # 제거해야 하는 바위 수가 n개 이하라면 mid라는 최소 거리는 만들 수 있음
        #
        # "가능한 최소 거리 중 최댓값"을 찾고 있으므로 더 큰 값도 가능한지 오른쪽 탐색
        if remove_rock <= n:
            left = mid + 1

        # n개보다 많이 제거해야 한다면 mid가 너무 큰 값이라는 뜻
        # 따라서 더 작은 값을 탐색
        else:
            right = mid - 1

    # 반복문 종료 후
    # right = 가능한 값 중 가장 큰 값
    # left  = 그보다 1 큰 불가능한 값
    # 원하는 것은 가능한 최소 거리의 최댓값이므로 right 반환
    return right