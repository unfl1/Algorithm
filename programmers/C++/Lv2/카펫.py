def solution(brown, yellow):
    for i in range(1, int(yellow**0.5) + 1):
        if yellow%i != 0:
            continue

        x = yellow // i
        y = i

        if (x+2) * (y+2) == brown+yellow:
            return [x+2, y+2]