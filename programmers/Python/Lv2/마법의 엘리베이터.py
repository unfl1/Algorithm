def solution(storey):
    answer = 0

    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10

        if digit > 5 or (digit == 5 and next_digit >= 5):
            # 올려서 현재 자릿수를 0으로 만들기
            answer += 10 - digit
            storey = storey // 10 + 1
        else:
            # 내려서 현재 자릿수를 0으로 만들기
            answer += digit
            storey //= 10

    return answer