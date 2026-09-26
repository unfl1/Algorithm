def solution(s):
    answer = [0,0]
    
    while s!='1':
        answer[1]+=(s.count('0'))
        
        change = s.count('1')
        s = bin(change)[2:]
        
        answer[0]+=1
        
    return answer