def solution(n, words):
    check = set()
    person=0
    
    for i in range(0, len(words)-1):
        if words[i][-1] != words[i+1][0] or words[i+1] in check:
            person = i+1
            return [person%n + 1, person//n + 1]
            
        check.add(words[i])
        
    return [0,0]

        