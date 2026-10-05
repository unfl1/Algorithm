def solution(number, k):
    cur = 0
    stack = []

    while cur < len(number):
        while stack and k > 0 and stack[-1] < number[cur]:
            stack.pop()
            k-=1

        stack.append(number[cur])
        cur+=1
        
    # 앞에 작은 수가 없어서 제거를 못할 수도 있음
    # 2개 제거인데 98765라면 -> k=2, stack=['9','8','7','6','5']
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)