def solution(sequence, k):
    left = 0
    right = 0
    total = sequence[0]

    answer = [0, len(sequence) - 1]

    while right < len(sequence):
        if total < k:
            right += 1
            if right < len(sequence):
                total += sequence[right]
        elif total > k:
            total -= sequence[left]
            left += 1
        else:  # total == k
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            total -= sequence[left]
            left += 1

    return answer