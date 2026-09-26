def solution(elements):
    n = len(elements)
    ex = elements * 2
    result = set()

    for length in range(1, n+1):  
        for start in range(n):      
            s = sum(ex[start:start+length])
            result.add(s)

    return len(result)