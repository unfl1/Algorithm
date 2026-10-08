def solution(arr):
    def compress(x, y, size):
        # 첫 시작 수
        val = arr[x][y]
        same = True
        # size 만큼 확인해보고
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != val: # 첫 시작 수랑 다르면
                    same = False # 공통 수 아님
                    break
            if not same:
                break

        if same: # 만약 다 같은 수였다면
            result[val] += 1
        else: # 아니라면
            half = size // 2 # 사이즈를 반으로 줄여서
            compress(x, y, half) #11시 방향
            compress(x, y + half, half) #1시 방향
            compress(x + half, y, half) #7시 방향
            compress(x + half, y + half, half) #5시 방향

    result = [0, 0]
    compress(0, 0, len(arr))
    return result