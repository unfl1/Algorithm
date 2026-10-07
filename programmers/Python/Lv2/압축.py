def solution(msg):
    answer = []
    
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    words = {}
    for i in range(len(alphabet)):
        words[alphabet[i]] = i+1
        
    idx = 27
    cur = 0
    
    while cur<len(msg):
        now = ""
        nxt = cur
        
        while nxt<len(msg):
            now+=msg[nxt]
            
            if now in words:
                nxt+=1
            else:
                break
        
        if nxt==len(msg):
            answer.append(words[now])
            break
            
        words[now]=idx
        idx+=1   
        answer.append(words[now[:-1]])  
        
        cur = nxt
    
    return answer