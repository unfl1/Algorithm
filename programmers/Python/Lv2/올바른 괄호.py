def solution(s):

    stack = []

    for i in s:
        if i=='(':
            stack.append("(")
        else:
            if len(stack)==0:
                return False
        
            if stack[-1]=='(':
                stack.pop()
            else:
                return False

    return len(stack)