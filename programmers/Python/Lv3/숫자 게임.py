def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    answer = 0
    point_a, point_b = 0, 0
    
    while point_a!=len(A) and point_b!=len(B):
        if B[point_b] > A[point_a]:
            answer+=1
            point_b+=1
            point_a+=1
        else:
            point_a+=1
            
    return answer