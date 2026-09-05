def solution(triangle):

    # 꼭대기부터 dp 시작
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 맨 왼쪽
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            # 맨 오른쪽
            elif j==len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][j-1]
            # 나머지는 양쪽 위 중 더 큰 값
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
            
    return max(triangle[len(triangle)-1])