def solution(arr1, arr2):
    y = len(arr1)
    x = len(arr2[0])
    length = len(arr1[0])
    
    answer = [[0]*x for _ in range(y)]
    
    for i in range(y):
        for j in range(x):
            for k in range(length):
                answer[i][j]+=(arr1[i][k]*arr2[k][j])
                
    return answer