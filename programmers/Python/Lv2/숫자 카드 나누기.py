def gcd(a, b):
    while b!=0:
        a, b = b, a%b
        
    return a


def arr_gcd(arr):
    res = arr[0]
    
    for i in range(1, len(arr)):
        res = gcd(res, arr[i])
        
    return res


def check(arr, g):
    for i in arr:
        if i%g == 0:
            return False
        
    return True


def solution(arrayA, arrayB):
    
    A = arr_gcd(arrayA)
    B = arr_gcd(arrayB)
    
    if check(arrayA, B) or check(arrayB, A):
        return max(A, B)
    else:
        return 0
    