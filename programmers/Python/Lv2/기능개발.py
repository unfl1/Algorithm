def solution(progresses, speeds):
    answer = []
    cur=0

    while cur<len(progresses):
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        
        cnt = 0

        while cur<len(progresses) and progresses[cur]>=100:
            cur+=1
            cnt+=1
            
        if cnt>0:
            answer.append(cnt)
        
    return answer