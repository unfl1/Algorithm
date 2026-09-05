def solution(nums):

    ponketmon={}

    for i in nums:
        ponketmon[i]=ponketmon.get(i,0)+1

    return min(len(ponketmon), len(nums)/2)