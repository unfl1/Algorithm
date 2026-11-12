def solution(sticker):
    
    N = len(sticker)
    
    if N==1:
        return sticker[0]
    
    # 첫번째 스티커를 선택
    dp1 = [0] * N
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, N):
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
    
    # 첫번째 스티커를 선택 X
    dp2 = [0] * N
    dp2[1] = sticker[1]
    for i in range(2, N):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
        
    # dp1[N-2] -> 첫번째 스티커를 선택했다면 마지막 스티커 선택 X
    # dp2[N-1] -> 첫번째 스티커를 선택했다면 마지막 스티커 선택
    return max(dp1[N-2], dp2[N-1])