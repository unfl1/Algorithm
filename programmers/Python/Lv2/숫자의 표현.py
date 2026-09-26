def solution(n):
    answer=0
    for start in range(1,n+1):
        sum_num=0
        while sum_num<n:
            sum_num+=start
            start+=1
            
        if sum_num==n:
            answer+=1
            
    return answer