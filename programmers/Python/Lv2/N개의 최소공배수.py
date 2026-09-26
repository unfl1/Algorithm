def solution(arr):
    gcd_nums = arr[0]
    for i in range(1, len(arr)):
        gcd_nums = gcd(gcd_nums,arr[i])
    
    mul = arr[0]
    for i in range(1, len(arr)):
        mul = lcm(mul,arr[i])
        
    return mul

def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return a*b/gcd(a,b)