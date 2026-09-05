def solution(progresses, speeds):
    answer=[]
    cur=0

    while (cur!=len(speeds)):
        for i in range(cur, len(speeds)):
            progresses[i]+=speeds[i]

        cnt=0

        while (cur<len(progresses) and progresses[cur]>=100):
            cnt+=1
            cur+=1

        if cnt > 0:
            answer.append(cnt)

    return answer